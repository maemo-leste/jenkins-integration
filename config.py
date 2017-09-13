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

    # Maemo has its own gtk2 fork
    'gtk': {}, # maybe call the job maemo-gtk2?

    # 
    'libmatchbox2': {},

    #
    'mce-dev': {},

    #
    'libhildonmime': {},

    #
    'cityinfo': {},

    #
    'clockd': {},

    #
    'libosso': {},

    #
    'icd2-osso-ic-dev': {},

    #
    'libconic': {},

    #
    'osso-systemui-dbus-dev': {},

    #
    'libdsme': {},

    #
    'statusbar-alarm-dbus-api': {},

    #
    'hildon': {},

    #
    'maemo-system-services': {},

    #
    'osso-core-config': {},

    #
    'osso-af-utils': {},

    #
    'osso-af-startup': {},

    #
    'osso-af-settings': {},

    #
    'ke-recv-extra': {},

    #
    'upstart-dev': {},

    # fixed with a hack, remember to fix properly
    # https://git.devuan.org/maemo/clipboard-manager/commit/df4d727d4dc95cd01014dc388c9c1088c8a296f5
    'clipboard-manager': {},

    #
    'libhildondesktop': {},

    #
    'alarmd': {},

    #
    'maemo-launcher': {},

    #
    'profiled': {},

    #
    'hildon-desktop': {},
}

def get_jobs():
    jobs = {}
    for job, args in _jobs.items():
        repo_name = args.get('repo-name', job)
        host = args.get('host', DEFAULT_HOST) % repo_name
        releases = args.get('releases', DEFAULT_RELEASES)
        
        jobs[job] = dict(repo_name=repo_name, host=host, releases=releases)

    return jobs
