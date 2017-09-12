DEFAULT_RELEASES = {'kawai': 'jessie'}
DEFAULT_HOST = 'https://git.devuan.org/maemo/%s'


"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'some-MAEMO-release': 'DEVUAN-upstream-release'}
"""

_jobs =  {
    # comment here
    'libcal': {
        #'releases': {
        #    # we should use these when building, not creating/deleting
        #    # ${release} : ${distribution} (in a jenkins job)
        #    # 'kawai': 'jessie',
        #    # 'rishi': 'ascii',
        #},
    },

    # 
    'iphbd': {},

    # 
    'libmatchbox2': {},

    # Maemo has its own gtk2 fork
    'gtk': {}, # maybe call the job maemo-gtk2?

    # 
    'mce-dev': {},
}

def get_jobs():
    jobs = {}
    for job, args in _jobs.items():
        repo_name = args.get('repo-name', job)
        host = args.get('host', DEFAULT_HOST) % repo_name
        releases = args.get('releases', DEFAULT_RELEASES)
        
        jobs[job] = dict(repo_name=repo_name, host=host, releases=releases)

    return jobs
