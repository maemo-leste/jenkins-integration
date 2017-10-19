#!/usr/bin/env python3

from subprocess import check_output

from sys import exit
from time import sleep

from config import get_jobs

def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Build all jobs')

    parser.add_argument('-e', '--exclude', action='append',
                        help='Exclude package from build',
                        default=[])
    parser.add_argument('-p', '--pretend', action='store_true',
                        default=False, help='Pretend')
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Debug output')

    args = parser.parse_args()

    jobs = get_jobs().keys()

    # Sanity check
    for exclude in args.exclude:
        if exclude not in jobs:
            print('Cannot exclude %s - not a valid job' % exclude)
            exit(1)

    for job in jobs:
        if job not in args.exclude:
            if args.pretend:
                print('Would build: %s' % job)
                continue

            print('Building: %s.' % job)
            out = check_output(['./run-job.py', '-j', job])
            job_no = out.strip().decode('utf-8')
            job_no = int(job_no.replace('Build number:', ''))
            if args.debug:
                print('Got job number:', job_no)

            sleep(10.)

            check_output(['./wait-build.py', job, '--buildno', str(job_no)])
            
            print('%s OK.' % job)



if __name__ == '__main__':
    main()
