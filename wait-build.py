#!/usr/bin/env python3

from argparse import ArgumentParser

import requests

from jenkins import Jenkins
from config import get_jobs

from jenkins_creds import (jenkins_host, jenkins_user, jenkins_pass)

from pprint import pprint
from time import sleep

SLEEP = 5.0

# HACKY
REPOS_SPAWNED = 3

def wait_for_source_job(japi, jobname, buildno):
    while True:
        job = japi.get_build_info(jobname + '-source', buildno, depth=2)
        if not job['building']:
            break
        print('Waiting for source to be done building')
        sleep(SLEEP)

    assert job['result'] == 'SUCCESS', 'Source job result was not SUCCESS: %s' % job['result']

    # Hacky
    print('Waiting for binaries to be started')
    sleep(10)
    job = japi.get_build_info(jobname + '-source', buildno, depth=2)

    binaries_name = None
    binaries_buildno = None

    ja = job['actions']
    for i in ja:
        if '_class' in i and i['_class'] == 'hudson.plugins.parameterizedtrigger.BuildInfoExporterAction':
            for proj in i['triggeredProjects']:
                assert binaries_name is None
                assert binaries_buildno is None

                binaries_name = proj['name']
                builds = proj['builds']
                for build in builds:
                    binaries_buildno = build['number']
                    break

    return binaries_name, binaries_buildno


def wait_for_binaries_job(japi, jobname, buildno):
    while True:
        job = japi.get_build_info(jobname, buildno, depth=3)
        if not job['building']:
            break
        print('Waiting for binaries to be done building')
        sleep(SLEEP)

    assert job['result'] == 'SUCCESS', 'Job %s result was not SUCCESS' % job['result']

    # Hacky
    print('Waiting for repos to be started')
    sleep(10)

    job = japi.get_build_info(jobname, buildno, depth=3)

    repos_build_numbers = []
    repos_build_name = None
    for run in job['runs']:
        assert run['result'] == 'SUCCESS'
        actions = run['actions']
        for i in actions:
            if '_class' in i and i['_class'] == 'hudson.plugins.parameterizedtrigger.BuildInfoExporterAction':
                for proj in i['triggeredProjects']:
                    if repos_build_name is None:
                            repos_build_name = proj['name']
                    else:
                        assert repos_build_name == proj['name'], 'Different triggered project name?'

                    for build in proj['builds']:
                        # HACKY
                        if len(repos_build_numbers) == REPOS_SPAWNED:
                            break

                        build_no = build['number']
                        repos_build_numbers.append(build_no)


    return repos_build_name, repos_build_numbers


def wait_for_repos_job(japi, jobname, buildno):
    while True:
        job = japi.get_build_info(jobname, buildno, depth=1)
        if not job['building']:
            break
        print('Waiting for repos to be done building')
        sleep(SLEEP)

    assert job['result'] == 'SUCCESS', 'Job %s result was not SUCCESS' % job['result']


def main():
    parser = ArgumentParser()
    parser.add_argument('jobname', type=str, default=None)
    parser.add_argument('--buildno', type=int)

    args = parser.parse_args()

    japi = Jenkins(jenkins_host, username=jenkins_user, password=jenkins_pass)

    # Input: jobname (without -source, etc)
    # 1. Get info for -source job (and check 'result' == 'SUCCESS')
    # 2. Get matching -binaries job (and check 'result' == 'SUCCESS')
    # 3. Get runs for -binaries job (and check 'result' == 'SUCCESS')
    # 4. For each -binaries run, find repos jobs (we will find all repos jobs for all runs, but we deal with that)
    # 5. With each repos job, check 'result' == 'SUCCESS'.

    binaries_name, binaries_buildno = wait_for_source_job(japi, args.jobname, args.buildno)
    print('binaries_name, binaries_buildno:', binaries_name, binaries_buildno)
    print('Source OK')

    repos_name, repos_buildnos = wait_for_binaries_job(japi, binaries_name, binaries_buildno)
    assert len(repos_buildnos) > 0
    print('repos_buildnos:', repos_buildnos)
    print('Binaries OK')

    for buildno in repos_buildnos:
        wait_for_repos_job(japi, repos_name, buildno)
    print('Repos OK')


if __name__ == '__main__':
    main()
