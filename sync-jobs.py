#!/usr/bin/env python3

from argparse import ArgumentParser

from jenkins import Jenkins
from config import get_jobs

from jenkins_creds import (jenkins_host, jenkins_user, jenkins_pass)

"""
API Reference:
japi.create_job()
japi.build_job()
japi.reconfig_job()
japi.rename_job()
japi.disable_job()
japi.enable_job()
japi.delete_job()
japi.cancel_queue()
japi.job_exists()
japi.get_job_config()
"""

def _create_archvals(arches):
    ar = ['<string>%s</string>' % a for a in arches]
    return '\t' + '\n\t'.join(ar)


def create_job_config(japi, jobs, jobname):
    job_info = jobs[jobname]

    source = '%s-source' % jobname
    binaries = '%s-binaries' % jobname
    repos = '%s-repos' % jobname

    archval = _create_archvals(job_info['arches'])
    labelval = archval

    replacements = [('DESCRIPTION', job_info['repo_name']),
                    ('GITURL', job_info['host']),
                    ('JOBNAME', binaries),
                    ('COPYFROM', source),
                    ('REPOSJOB', repos),
                    ('ARCHVALUES', archval),
                    ('LABELVALUES', labelval)]


    if job_info['arches'] == ['all']:
        bin_job = open('xmls/binaries-all.xml', encoding='utf-8').read()
        rep_job = open('xmls/repos-all.xml', encoding='utf-8').read()
    else:
        bin_job = open('xmls/binaries-arch.xml', encoding='utf-8').read()
        rep_job = open('xmls/repos-arch.xml', encoding='utf-8').read()

    src_job = open('xmls/source.xml', encoding='utf-8').read()

    for r in replacements:
        src_job = src_job.replace('{{{%s}}}' % r[0], r[1])
        bin_job = bin_job.replace('{{{%s}}}' % r[0], r[1])
        rep_job = rep_job.replace('{{{%s}}}' % r[0], r[1])

    #if 'https://github.com/maemo-leste-extras/' in job_info['host']:
    if 'https://git.maemo.org/leste-extras/' in job_info['host']:
        src_job = src_job.replace('<defaultValue>leste</defaultValue>',
                                  '<defaultValue>extras</defaultValue>')
        bin_job = bin_job.replace('<defaultValue>leste</defaultValue>',
                                  '<defaultValue>extras</defaultValue>')
        rep_job = rep_job.replace('<defaultValue>leste</defaultValue>',
                                  '<defaultValue>extras</defaultValue>')



    return (source, src_job), (binaries, bin_job), (repos, rep_job)


def add_jobs(japi, jobs, jobname):
    sources, binaries, repos = create_job_config(japi, jobs, jobname)

    return japi.create_job(sources[0], sources[1]), \
        japi.create_job(binaries[0], binaries[1]), \
        japi.create_job(repos[0], repos[1])


def del_jobs(japi, jobs, jobname):
    source = '%s-source' % jobname
    binaries = '%s-binaries' % jobname
    repos = '%s-repos' % jobname

    # TODO: remove debs and metadata from /srv/repository

    return japi.delete_job(source), japi.delete_job(binaries), japi.delete_job(repos)


def reconfig_jobs(japi, jobs, jobname):
    sources, binaries, repos = create_job_config(japi, jobs, jobname)

    return japi.reconfig_job(sources[0], sources[1]), \
        japi.reconfig_job(binaries[0], binaries[1]), \
        japi.reconfig_job(repos[0], repos[1])


def main():
    parser = ArgumentParser()
    parser.add_argument('-j', '--job', type=str, nargs='*', default=list())
    parser.add_argument('-s', '--sync', action='store_true')
    parser.add_argument('-r', '--reconfig', action='store_true')
    parser.add_argument('-n', '--dry_run', action='store_true')

    args = parser.parse_args()

    japi = Jenkins(jenkins_host, username=jenkins_user, password=jenkins_pass)
    all_jobs = set([x['name'] for x in japi.get_all_jobs()])

    # list of jobs we don't want to touch
    exceptions = [
        'jenkins-debian-glue',
        'leste-image-virtual',
        'leste-image-n900',
        'leste-image-droid4',
        'leste-image-pinephone',
        'leste-image-pinetab',
        'leste-image-raspi3-64bit',
        'leste-image-raspi4-64bit',
        'leste-image-raspi2',
        'leste-image-arm64-generic',
        'leste-image-turbox-twister',
        'leste-image-olimex-lime2',
    ]

    jobs = get_jobs()

    if args.job:
        jobs = dict([(x, jobs[x]) for x in args.job])


    if args.sync and args.reconfig:
        print('Can not sync and reconfig. Choose one.')
        return

    if args.reconfig:
        for j in jobs:
            if j in exceptions:
                continue
            if args.dry_run:
                print('WOULD RECONFIG:', j)
                continue
            print('Reconfiguring job:', j)
            reconfig_jobs(japi, jobs, j)
        return

    if args.sync:
        source_bin_jobs = [(key + '-source', key+'-binaries') for key in jobs.keys()]
        config_jobs = []
        for (source, bina) in source_bin_jobs:
            config_jobs.append(source)
            config_jobs.append(bina)

        all_config_jobs = set(config_jobs)

        jobs_to_remove = all_jobs - all_config_jobs
        jobs_to_add = all_config_jobs - all_jobs

        def filter_jobs(jobs):
            return list(map(lambda x: x[:-len('-source')], filter(lambda x: x.endswith('-source'), jobs)))

        for j in filter_jobs(jobs_to_remove):
            if j in exceptions:
                continue
            if args.dry_run:
                print('WOULD REMOVE:', j)
                continue
            print('Deleting job:', j)
            del_jobs(japi, jobs, j)

        for j in filter_jobs(jobs_to_add):
            if j in exceptions:
                continue
            if args.dry_run:
                print('WOULD ADD:', j)
                continue
            print('Adding job:', j)
            add_jobs(japi, jobs, j)


if __name__ == '__main__':
    main()
