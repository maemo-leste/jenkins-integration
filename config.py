from collections import OrderedDict

DEFAULT_RELEASES = {
    'leste': [
        'ascii',
        'ascii-devel',
        'beowulf'
    ],
    'extras': [
        'ascii',
        'beowulf'
    ],
}
DEFAULT_HOST = 'https://github.com/maemo-leste/%s'
DEFAULT_ARCHES = ['amd64', 'armhf', 'arm64']


"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'maemo-leste-repo': 'devuan-distribution'}
"""

_jobs = OrderedDict([
    #
    ('maemo-keyring', {
        'arches': ['all'],
    }),

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
    ('mce-dev', {}),

    #
    ('libhildonmime', {}),

    #
    ('cityinfo', {}),

    #
    ('clockd', {}),

    #
    ('libosso', {}),

    #
    ('icd2-osso-ic-dev', {}),

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
    ('libhildon', {}), # XXX: needs bayamo fixes

    #
    ('maemo-system-services', {}),

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
    ('osso-af-settings', {}),

    #
    ('ke-recv-extra', {}),

    #
    ('clipboard-manager', {}),  # bayamo current

    #
    ('libhildondesktop', {}),

    #
    ('alarmd', {}), # already ported to bayamo

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
    ('osso-systemui-modechange', {}),

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

    # n900-specific from spinal
    ('hildon-desktop-n900', {
        'arches': ['armhf'],
    }),

    # n900-specific from spinal
    ('clutter-0.8', {
        'arches': ['armhf'],
    }),

    # n900 specific from spinal
    ('libmatchbox2-n900', {
        'arches': ['armhf'],
    }),

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
    ('theme-default-settings', {
        'arches': ['all'],
    }),

    #
    ('hildon-base', {
        'arches': ['all'],
    }),

    #
    ('hildon-meta', {
        'arches': ['all'],
    }),

    #
    ('hildon-connectivity-meta', {
        'arches': ['all'],
    }),

    #
    ('status-menu-applet-profiles', {}),

    #
    ('xorg-server', {}),

    #
    ('status-area-applet-battery', {}),

    #
    ('ofono', {}),

    # pavel's droid4 ofono fork
    ('ofono-d4', {}),

    #
    ('connui-common', {}),

    #
    ('maemo-security-certman', {}),

    #
    ('libcomapp', {}),

    #
    ('maemo-security-certman-applet', {}),

    #
    ('connui-internet', {}),

    #
    ('hildon-status-bar-usb', {}),

    #
    ('libicd-network-dummy', {}),

    #
    ('libicd-network-usb', {}),

    #
    ('icd2-settings-default', {
        'arches': ['all'],
    }),

    #
    ('libusbgx', {}),

    #
    ('wl1251-cal', {}),

    #
    ('maemo-multimedia-tone-generator', {}),

    #
    ('libicd-network-ipv4', {}),

    #
    ('libconbtui', {
        'arches': ['all'],
    }),

    #
    ('connui-wlan', {}),

    ('libicd-network-wpasupplicant', {}),

    #
    ('status-area-orientationlock-applet', {}),

    #
    ('n9xx-linux', {
        'arches': ['armhf'],
    }),


    #
    ('upower', {}),

    #
    ('libscconf', {}),

    #
    ('hildon-input-method-framework', {}),

    #
    ('hildon-input-method', {}),

    #
    ('libimlayouts', {}),

    #
    ('libimengines', {}),

    #
    ('hildon-im-vkbrenderer3', {}),

    #
    ('hildon-input-method-configurator', {}),

    #
    ('hildon-input-method-plugins', {}),

    #
    ('osso-applet-textinput', {}),

    #
    ('hildon-input-meta', {
        'arches': ['all'],
    }),

    #
    ('mafw', {}),

    #
    ('mafw-shared', {}),

    #
    ('mafw-iradio-source', {}),

    #
    ('mafw-upnp-source', {}),

    #
    ('hildon-usb-gadgets', {}),

    #
    ('ke-recv', {}),

    # mesa for lime2 and a33
    ('mesa', {
        'arches': ['armhf', 'arm64'],
    }),

    # glib with fixes
    ('glib', {}),

    #
    ('osso-calculator-engine', {}),

    #
    ('unicsy_demo', {
        'arches': ['all'],
    }),

    #
    ('libcmtspeechdata', {
        'arches': ['armhf'],
    }),

    #
    ('droid4-linux', {
        'arches': ['armhf'],
    }),

    #
    ('pine64-kernel', {
        'arches': ['arm64'],
    }),

    #
    ('rtl8723cs', {
        'arches': ['all'],
    }),

    #
    ('ti-omap3-sgx', {
        'arches': ['armhf'],
    }),

    #
    ('xf86-video-pvrsgx', {
        'arches': ['armhf'],
    }),

    #
    ('firmware-ti-bluetooth', {
        'arches': ['all'],
    }),

    #
    ('connui-cellular', {}),

    #
    ('libofono', {}),

    #
    ('libicd-network-ofono', {}),

    #
    ('libglibutil', {}),

    #
    ('libgofono', {}),

    #
    ('hildon-notify', {}),

    #
    ('statusbar-alarm', {}),

    #
    ('rtcom-eventlogger', {}),

    # ********************* Python stuff
    #
    ('pygtk', {}),

    #
    ('python-hildon', {}),

    #
    ('python-osso', {}),

    #
    ('python-hildondesktop', {}),

    #
    ('hildon-application-manager', {
    }),

    #
    ('hildon-application-manager-settings-standard', {
    }),

    #
    ('osso-pdf-viewer', {
    }),

    #
    ('iso-codes-locale-resolver', {}),

    #
    ('surf2', {}),

    # ********************* Extras start here?
    #
    ('libsdl', {}),

    #
    ('sdlgles', {}),

    #
    ('osso-games-startup', {}),

    #
    ('hildon-games-wrapper', {}),

    #
    ('xkb-data', {
        'arches': ['all'],
    }),

    # Extra pkg
    ('binaryclock-plugin', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('wifi-signal-applet', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('simple-brightness-applet', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('brainparty', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('brainparty-data', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('scummvm', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('crazyparking', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('osso-mahjong', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('mypaint', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('uae4all', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sojourner', {
        'host': 'https://github.com/maemo-leste-extras/%s',
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
