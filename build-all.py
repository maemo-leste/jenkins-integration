#!/usr/bin/env python3

from subprocess import check_output

from sys import exit
from time import sleep

from config import get_jobs, DEFAULT_RELEASES

def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Build all jobs')

    parser.add_argument('-e', '--exclude', action='append',
                        help='Exclude package from build',
                        default=[])
    parser.add_argument('-s', '--startfrom', type=str,
                        help='Start build from this package',
                        default=None)
    parser.add_argument('-r', '--release', action='append',
                        help='Releases to build for',
                        default=[])
    parser.add_argument('-p', '--pretend', action='store_true',
                        default=False, help='Pretend')
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Debug output')

    args = parser.parse_args()

    jobs = get_jobs().keys()

    releases = args.release
    if not len(releases):
        releases = DEFAULT_RELEASES.keys()

    # Sanity check
    for exclude in args.exclude:
        if exclude not in jobs:
            print('Cannot exclude %s - not a valid job' % exclude)
            exit(1)

    startfrom = 0
    if args.startfrom:
        if args.startfrom not in jobs:
            print('%s is not a valid job' % args.startfrom)
            exit(1)
        startfrom = list(jobs).index(args.startfrom)

    for job in list(jobs)[startfrom:]:
        for release in releases:
            if job not in args.exclude:
                if args.pretend:
                    print('Would build: %s for %s' % (job, release))
                    continue
    
                print('Building: %s for %s.' % (job, release))
                out = check_output(['./run-job.py', '-j', job, '-d', release])
                job_no = out.strip().decode('utf-8')
                job_no = int(job_no.replace('Build number:', ''))
                if args.debug:
                    print('Got job number:', job_no)
    
                sleep(10.)
    
                check_output(['./wait-build.py', job, '--buildno', str(job_no)])
                
                print('%s OK.' % job)
    
                sleep(2) # just in case ;)



if __name__ == '__main__':
    main()
