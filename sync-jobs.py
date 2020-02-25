#!/usr/bin/env python3

from argparse import ArgumentParser

from jenkins import Jenkins
from config import get_jobs

from jenkins_creds import (jenkins_host, jenkins_user, jenkins_pass)


def _create_archvals(arches):
    ar = ['<string>%s</string>' % a for a in arches]
    return '\t' + '\n\t'.join(ar)


def add_jobs(japi, jobs, jobname):
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

    return japi.create_job(source, src_job), japi.create_job(binaries, bin_job), \
        japi.create_job(repos, rep_job)


def del_jobs(japi, jobs, jobname):
    source = '%s-source' % jobname
    binaries = '%s-binaries' % jobname
    repos = '%s-repos' % jobname

    # TODO: remove debs and metadata from /srv/repository

    return japi.delete_job(source), japi.delete_job(binaries), japi.delete_job(repos)


def reconfig_jobs(japi, jobs, jobname):
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

    src_job = open('source.xml', encoding='utf-8').read()
    bin_job = open('binaries.xml', encoding='utf-8').read()
    rep_job = open('repos.xml', encoding='utf-8').read()

    for r in replacements:
        src_job = src_job.replace('{{{%s}}}' % r[0], r[1])
        bin_job = bin_job.replace('{{{%s}}}' % r[0], r[1])
        rep_job = rep_job.replace('{{{%s}}}' % r[0], r[1])

    return japi.reconfig_job(source, src_job), japi.reconfig_job(binaries, bin_job), \
        japi.reconfig_job(repos, rep_job)


def main():
    parser = ArgumentParser()
    parser.add_argument('-l', '--list-something', action='store_true')
    parser.add_argument('-s', '--sync', action='store_true')
    parser.add_argument('-r', '--reconfig', action='store_true')
    parser.add_argument('-n', '--dry_run', action='store_true')

    args = parser.parse_args()

    japi = Jenkins(jenkins_host, username=jenkins_user, password=jenkins_pass)
    all_jobs = set([x['name'] for x in japi.get_all_jobs()])
    exceptions = ['jenkins-debian-glue']  # list of jobs we don't want to touch
    jobs = get_jobs()

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
        # TODO: we need to compare repo names and everything else later (can pickle that to a file)

        # from lxml import objectify
        # jobxml = japi.get_job_config(jobname)
        # tree = objectify.fromstring(jobxml)

        # compare:
        #   * repo_name
        # tree.builders['hudson.plugins.parameterizedtrigger.TriggerBuilder']['configs']['hudson.plugins.parameterizedtrigger.BlockableBuildTriggerConfig']['projects']
        #   * host
        # tree.scm.userRemoteConfigs['hudson.plugins.git.UserRemoteConfig']['url']
        #   * description
        # tree.description


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


"""
jenk.create_job()
jenk.build_job()
jenk.reconfig_job()
jenk.rename_job()
jenk.disable_job()
jenk.enable_job()
jenk.delete_job()
jenk.cancel_queue()
jenk.job_exists()
jenk.get_job_config()
"""
