from collections import OrderedDict

DEFAULT_RELEASES = {
    'leste': [
        'ascii',
        'ascii-devel',
        'beowulf',
        'beowulf-devel',
        'beowulf-experimental',
        'stretch',
        'buster',
    ],
    'extras': [
        'ascii',
        'beowulf',
        'beowulf-devel',
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

    # forked for openrc
    ('insserv', {}),

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
    ('osso-systemui-devlock', {}),

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
    ('hildon-desktop-clutter-1.x', {}),

    #
    ('clutter-0.8', {}),

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
    ('leste-config', {
        'arches': ['all'],
    }),

    #
    ('eg25-manager', {
        'arches': ['arm64'],
    }),

    #
    ('pinephone-modem-config', {
        'arches': ['all'],
    }),

    #
    ('hildon-connectivity-meta', {
        'arches': ['all'],
    }),

    #
    ('status-menu-applet-profiles', {}),

    #
    ('xorg-server', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('alsa-lib', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('alsa-utils', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('telepathy-glib', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('status-area-applet-battery', {}),

    #
    ('ofono', {}),

    # pavel's droid4 ofono fork
    ('ofono-d4', {}),

    #
    ('atinout', {}),

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
    ('sunxi-linux', {
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

    # glib with fixes
    ('glib', {}),

    #
    ('osso-calculator-engine', {}),

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
    ('pine64-uboot', {
        'arches': ['all'],
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

    # omap driver for droid4
    ('xf86-video-omap', {
        'arches': ['armhf'],
    }),

    #
    ('pvr-omap4', {
        'arches': ['armhf'],
    }),

    #
    ('libdri2', {
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

    #
    ('rtcom-eventlogger-ui', {}),

    #
    ('rtcom-eventlogger-plugins', {}),

    #
    ('osso-abook', {}),

    # ********************* Python stuff
    #
    ('pygtk', {}),

    #
    ('python-hildon', {}),

    #
    ('python-osso', {}),

    #
    ('python-alarm', {}),

    #
    ('python-hildondesktop', {}),

    #
    ('gnome-python', {}),

    #
    ('hildon-application-manager', {
    }),

    #
    ('hildon-application-manager-settings-standard', {
        'arches': ['all'],
    }),

    #
    ('osso-pdf-viewer', {
    }),

    #
    ('iso-codes-locale-resolver', {}),

    #
    ('libglvnd', {}),

    #
    ('libdrm', {}),

    #
    ('mesa', {}),

    # ********************* Extras start here?
    #
    ('libsdl1.2', {}),

    #
    ('sdlgles', {}),

    #
    ('gl4es', {
        'arches': ['armhf'],
    }),

    #
    ('osso-games-startup', {}),

    #
    ('hildon-games-wrapper', {}),

    #
    ('hildon-control-panel-personalisation', {}),

    #
    ('hildon-theme-tools', {}),

    #
    ('hildon-theme-layout', {
        'arches': ['all'],
    }),

    #
    ('osso-applet-languageregional', {}),

    #
    ('droid4-pm', {
        'arches': ['all'],
    }),

    #
    ('droid4-battery-calibration', {
        'arches': ['all'],
    }),

    #
    ('xkb-data', {
        'arches': ['all'],
    }),

    #
    ('qtstyleplugins', {}),

    #
    ('qt-platform-maemo', {}),

    #
    ('ti-utils-wilink6', {
        'arches': ['armhf'],
    }),

    #
    ('droid4-wlanconfig', {
        'arches': ['all'],
    }),

    #
    ('maemo-input-sounds', {
    }),

    #
    ('maemo-audio', {
        'arches': ['all'],
    }),

    #
    ('iio-sensor-proxy', {}),

    #
    ('dbus-scripts', {
    }),

    #
    ('hildon-desktop-rotation-support', {
        'arches': ['all'],
    }),

    #
    ('libgq-gconf', {
    }),

    #
    ('clock-ui', {
    }),

    #
    ('evolution-data-server', {
    }),

    #
    ('syncevolution', {}),

    #
    ('eds-backend-telepathy', {
    }),

    #
    ('calendar-backend', {
    }),

    #
    ('qalendar', {
    }),

    #
    ('osso-calculator', {}),

    #
    ('clock', {}),

    #
    ('hildon-time-zone-chooser', {}),

    #
    ('applet-datetime', {}),

    #
    ('location-control', {}),

    #
    ('liblocation', {}),

    #
    ('location-daemon', {}),

    #
    ('python-location', {}),

    #
    ('pkg-gpsd', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    # Extra pkg
    ('surf2', {
        'host': 'https://github.com/maemo-leste-extras/%s',
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

    # Extra pkg
    ('pyfuelpad', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('9x9-sudoku', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('hildon-theme-marina', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('miku-theme', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('hildon-theme-matrix', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('hildon-theme-okuda', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('maeotp', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('quicknote', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('photolightmeter', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('personal-ip-address', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('countdowntimer', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('mihphoto', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sigstoped', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('qsigstoped', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('lirios-cmake-shared', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('lirios-fluid', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('lirios-calculator', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('lirios-files', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('profilesx', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('unicsy_demo', {
        'arches': ['all'],
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('dorian', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('iio-uinput', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('min', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('cal-home-widget', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('desktop-cmd-exec', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('hildon-theme-maemo-org', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('maep', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('syncevolution-frontend', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg
    ('zkgroup', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('signald', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('libpurple-signald', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # in main; necessary for anbox/cpu-features
    ('googletest', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    # Extra pkg
    ('cpu-features', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sdbus-cpp', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),
    # Extra pkg
    ('anbox-image', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('anbox', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sfeed', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sfeed-curses', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg (electrum dep)
    ('aiohttp-socks', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg (electrum dep)
    ('aiorpcx', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg (electrum dep)
    ('python-attrs', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg (electrum dep)
    ('python-ecdsa', {
        'host': 'https://github.com/maemo-leste-extras/%s',
        'arches': ['all'],
    }),

    # Extra pkg (electrum dep)
    ('zbar', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg (electrum dep)
    ('libsecp256k1', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg (electrum dep)
    ('protobuf', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg (deps above)
    ('electrum', {
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
