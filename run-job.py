#!/usr/bin/env python3

from argparse import ArgumentParser

from jenkins import Jenkins
from config import get_jobs, DEFAULT_RELEASES

from jenkins_creds import (jenkins_host, jenkins_user, jenkins_pass)


def main():
    parser = ArgumentParser()
    parser.add_argument('-j', '--jobname', type=str, default=None)
    parser.add_argument('-n', '--dry_run', action='store_true')
    parser.add_argument('-d', '--distro', type=str, default='all')  # maybe implement an 'all' logic?

    args = parser.parse_args()

    if args.distro not in DEFAULT_RELEASES:
        print('Distro unsupported. Use something from %s' % DEFAULT_RELEASES)
        return

    release = args.distro
    distribution = DEFAULT_RELEASES[release]

    japi = Jenkins(jenkins_host, username=jenkins_user, password=jenkins_pass)

    jobs = get_jobs()

    if args.dry_run:
        print('Would start:', args.jobname)
        return

    if args.jobname not in jobs:
        print('Job does not exist in config')
        return

    # Racy, but whatever
    nextjob = japi.get_job_info('%s-source' % args.jobname)['nextBuildNumber']
    job_no = japi.build_job('%s-source' % args.jobname,
                   {'release': release, 'distribution': distribution})
    print('Build number:', nextjob)

if __name__ == '__main__':
    main()
