from collections import OrderedDict

DEFAULT_RELEASES = {'leste': 'jessie', 'kawai': 'ascii'}
DEFAULT_HOST = 'https://github.com/maemo-leste/%s'
DEFAULT_ARCHES = ['amd64', 'armhf', 'armel']


"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'some-MAEMO-release': 'DEVUAN-upstream-release'}
"""

_jobs =  OrderedDict([
    # comment here
    ('libcal', {
        #'releases': {
        #    # we should use these when building, not creating/deleting
        #    # ${release} : ${distribution} (in a jenkins job)
        #    # 'leste': 'jessie',
        #},
    }),

    #
    ('iphbd', {}),

    # Maemo has its own gtk2 fork
    ('gtk', {}),

    #
    ('libmatchbox2', {}),

    #
    ('mce-dev', {
        'arches': ['all'],
    }),

    #
    ('libhildonmime', {}),

    #
    ('cityinfo', {}),

    #
    ('clockd', {}),

    #
    ('libosso', {}),

    #
    ('icd2-osso-ic-dev', {
        'arches': ['all'],
    }),

    #
    ('libconic', {}),

    #
    ('osso-systemui-dbus-dev', {
        'arches': ['all'],
    }),

    #
    ('libdsme', {}),

    #
    ('statusbar-alarm-dbus-api', {}),

    #
    ('hildon', {}),

    #
    ('maemo-system-services', {}),

    #
    #('osso-core-config', {
    #    'arches': ['all'],
    #}),

    #
    ('osso-af-utils', {}),

    #
    ('osso-af-startup', {
        'arches': ['all'],
    }),

    #
    ('hildon-initscripts', {
        'arches': ['all'],
    }),

    #
    ('osso-af-settings', {
        'arches': ['all'],
    }),

    #
    ('ke-recv-extra', {}),

    # fixed with a hack, remember to fix properly
    # https://git.devuan.org/maemo/clipboard-manager/commit/df4d727d4dc95cd01014dc388c9c1088c8a296f5
    ('clipboard-manager', {}),

    #
    ('libhildondesktop', {}),

    #
    ('alarmd', {}),

    #
    ('maemo-launcher', {}),

    #
    ('profiled', {}),

    #
    ('sapwood', {}),

    #
    ('hildon-theme-cacher', {}),

    #
    ('osso-icons', {
        'arches': ['all'],
    }),

    #
    ('dsme', {}),

    #
    ('osso-systemui', {}),

    #
    ('osso-systemui-powerkeymenu', {}),

    #
    ('osso-systemui-tklock', {}),

    #
    ('osso-systemui-devlock-dev', {
        'arches': ['all'],
    }),

    #
    ('osso-systemui-splashscreen-dev', {
        'arches': ['all'],
    }),

    #
    ('osso-systemui-modechange-dev', {
        'arches': ['all'],
    }),

    #
    ('libdevlock', {}),

    #
    ('osso-app-killer', {
        'arches': ['all'],
    }),

    #
    ('codelockui', {}),

    #
    ('hildon-control-panel', {}),

    #
    ('osso-applet-display', {}),

    #
    ('libplayback', {}),

    #
    ('hildon-plugins-notify-sv', {}),

    #
    ('osso-systemui-alarm', {}),

    #
    ('mce', {}),

    #
    ('osso-bookmark-engine', {}),

    #
    ('epeg', {}),

    #
    ('hildon-thumbnail', {}),

    #
    ('libhildonfm', {}),

    #
    ('hildon-home', {}),

    #
    ('hildon-desktop', {}),

    #
    ('osso-applet-notificationlight', {}),

    #
    ('osso-applet-devicelock', {}),

    #
    ('hildon-status-menu', {}),

    #
    ('osso-xterm', {}),

    #
    ('icd2', {}),

    #
    ('n9xx-xf86-video-fbdev-sgx', {}),

    #
    ('hildon-meta', {
        'arches': ['all'],
    }),
])

def get_jobs():
    jobs = OrderedDict()
    for job, args in _jobs.items():
        repo_name = args.get('repo-name', job)
        host = args.get('host', DEFAULT_HOST) % repo_name
        releases = args.get('releases', DEFAULT_RELEASES)
        arches = args.get('arches', DEFAULT_ARCHES)

        jobs[job] = dict(repo_name=repo_name, host=host, releases=releases,
                         arches=arches)

    return jobs
