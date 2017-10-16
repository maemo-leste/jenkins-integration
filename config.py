DEFAULT_RELEASES = {'leste': 'jessie'}
DEFAULT_HOST = 'https://github.com/maemo-leste/%s'


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
        #    # 'leste': 'jessie',
        #},
    },

    #
    'iphbd': {},

    # Maemo has its own gtk2 fork
    'gtk': {},

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
    'hildon-initscripts': {},

    #
    'osso-af-settings': {},

    #
    'ke-recv-extra': {},

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
    'sapwood': {},

    #
    'hildon-theme-cacher': {},

    #
    'osso-icons': {},

    #
    'dsme': {},

    #
    'osso-systemui': {},

    #
    'osso-systemui-powerkeymenu': {},

    #
    'osso-systemui-tklock': {},

    #
    'osso-systemui-devlock-dev': {},

    #
    'osso-systemui-splashscreen-dev': {},

    #
    'osso-systemui-modechange-dev': {},

    #
    'libdevlock': {},

    #
    'osso-app-killer': {},

    #
    'codelockui': {},

    #
    'hildon-control-panel': {},

    #
    'osso-applet-display': {},

    #
    'libplayback': {},

    #
    'hildon-plugins-notify-sv': {},

    #
    'osso-systemui-alarm': {},

    #
    'mce': {},

    #
    'osso-bookmark-engine': {},

    #
    'epeg': {},

    #
    'hildon-thumbnail': {},

    #
    'libhildonfm': {},

    #
    'hildon-home': {},

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
