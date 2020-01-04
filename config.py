from collections import OrderedDict

DEFAULT_RELEASES = {
    'leste': 'ascii',
    'leste-extra': 'ascii',
    'leste-devel': 'ascii-devel',
    'bayamo': 'beowulf',
}
DEFAULT_HOST = 'https://github.com/maemo-leste/%s'
#DEFAULT_ARCHES = ['amd64', 'armhf', 'armel', 'arm64']
DEFAULT_ARCHES = ['amd64', 'armhf', 'arm64']


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
    ('libhildon', {}),

    #
    ('maemo-system-services', {}),


    #
    #('osso-core-config', {
    #    'arches': ['all'],
    #}),

    #
    ('osso-af-utils', {}),

    #
    ('osso-af-startup', {      # bayamo current
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
    ('n9xx-xf86-video-fbdev-sgx', {
        'arches': ['armhf'],
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
    ('ti-omap3-sgx', {
        'arches': ['armhf'],
    }),

    #
    ('xf86-video-pvrsgx', {
        'arches': ['armhf'],
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
    ('python-hildondesktop', {}),

    #
    ('hildon-application-manager', {
    }),

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
    ('binaryclock-plugin', {
        #'releases': { 'leste-extra': 'ascii' }
    }),

    # Extra pkg
    ('wifi-signal-applet', {
        #'releases': { 'leste-extra': 'ascii' }
    }),

    # Extra pkg
    ('simple-brightness-applet', {
    }),

    # Extra pkg
    ('brainparty', {
    }),

    # Extra pkg
    ('scummvm', {
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
