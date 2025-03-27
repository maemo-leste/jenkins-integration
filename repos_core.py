from collections import OrderedDict
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
    ('libcal',
        {
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

    # We need this for matchbox
    ('clutter-0.8', {}),

    #
    ('libmatchbox2', {}),

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
    ('libhildon', {}),

    #
    ('libhildon3', {}),

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
    ('alarmd', {}),  # already ported to bayamo

    #
    ('maemo-launcher', {}),

    #
    ('profiled', {}),

    #
    ('profilesx', {}),

    #
    ('sapwood', {}),

    #
    ('hildon-theme-cacher', {}),

    #
    ('hildon-theme-alpha', {
        'arches': ['all'],
    }),

    #
    ('hildon-theme-beta', {
        'arches': ['all'],
    }),

    #
    ('hildon-theme-devel', {
        'arches': ['all'],
    }),

    #
    ('osso-icons', {
        'arches': ['all'],
    }),

    #
    ('ui-fonts', {
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
    ('hildon-meta-core', {
        'arches': ['all'],
    }),

    #
    ('leste-config', {
        'arches': ['all'],
    }),

    #
    ('eg25-manager', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
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

    # libsdl2 with --enable-video-kmsdrm
    ('libsdl2', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('status-area-applet-battery', {}),

    ## shared ofono for d4, pinephone, etc
    ('ofono', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    ## pavel's droid4 ofono fork
    #('ofono-d4', {}),

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
    ('libicd-provider-dummy', {}),

    #
    ('connui-dummy', {}),

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

    ##
    #('n9xx-linux', {
    #    'arches': ['armhf'],
    #}),

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
    ('iso-codes-locale-resolver', {}),

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
    ('mafw-tracker-source', {}),

    #
    ('mafw-upnp-source', {}),

    #
    ('hildon-usb-gadgets', {}),

    #
    ('ke-recv', {}),

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
    ('mapphone-kexecboot-config', {
        'arches': ['all'],
    }),

    ##
    #('rtl8723cs', {
    #    'arches': ['all'],
    #}),

    ##
    #('ti-omap3-sgx', {
    #    'arches': ['armhf'],
    #}),

    ##
    #('xf86-video-pvrsgx', {
    #    'arches': ['armhf'],
    #}),

    # omap driver for droid4
    ('xf86-video-omap', {
        'arches': ['armhf'],
    }),

    ##
    #('pvr-omap4', {
    #    'arches': ['armhf'],
    #}),

    #
    ('libdri2', {
        'arches': ['armhf'],
    }),

    #
    ('firmware-ti-bluetooth', {
        'arches': ['all'],
    }),

    # pocophone dependency
    ('qrtr', {
        'arches': ['arm64'],
    }),

    # pocophone dependency
    ('rmtfs', {
        'arches': ['arm64'],
    }),

    # pocophone dependency
    ('pd-mapper', {
        'arches': ['arm64'],
    }),

    # pocophone dependency
    ('tqftpserv', {
        'arches': ['arm64'],
    }),

    # pocophone kernel
    ('linux-beryllium', {
        'arches': ['arm64'],
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

    #
    ('osso-addressbook', {}),

    #
    ('osso-abook-home-applet', {}),

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
    ('hildon-application-manager', {}),

    #
    ('hildon-application-manager-settings-standard', {
        'arches': ['all'],
    }),

    #
    ('osso-pdf-viewer', {}),

    #
    ('libglvnd', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('libdrm', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('directx-headers', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('mesa', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('charge-mode', {}),

    #
    ('fbkeyboard', {}),

    # ********************* Extras start here?
    #
    ('libsdl1.2', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

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
    ('n900-pm', {
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
    ('maemo-input-sounds', {}),

    #
    ('maemo-audio', {
        'arches': ['all'],
    }),

    #
    ('iio-sensor-proxy', {}),

    #
    ('dbus-scripts', {}),

    ##
    #('hildon-desktop-rotation-support', {
    #    'arches': ['all'],
    #}),

    #
    ('libgq-gconf', {}),

    #
    ('clock-ui', {}),

    #
    ('evolution-data-server', {}),

    #
    ('syncevolution', {}),

    #
    ('eds-backend-telepathy', {}),

    #
    ('calendar-backend', {}),

    #
    ('qalendar', {}),

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
    ('location-status', {}),

    #
    ('location-ui', {}),

    #
    ('python-location', {}),

    #
    ('python-conic', {}),

    #
    ('python-mafw', {}),

    #
    ('osso-systemui-splashscreen', {}),

    #
    ('gps-nokia-n900', {
        'arches': ['armhf'],
    }),

    #
    ('pkg-gpsd', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('wpasupplicant', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('salutem', {}),

    #
    ('sphone', {}),

    #
    ('conversations', {}),

    #
    ('pulse-core', {}),

    #
    ('pulseaudio-modules-nemo', {}),

    #
    ('pulseaudio-module-cmtspeech-n9xx', {
        'arches': ['armhf'],
    }),

    #
    ('pulseaudio-policy-enforcement', {}),

    #
    ('libtrace-ohm', {}),

    #
    ('ohm', {}),

    #
    ('libprolog', {}),

    #
    ('libdres-ohm', {}),

    #
    ('ohm-rule-engine', {}),

    #
    ('policy-settings-common', {}),

    #
    ('libresource', {}),

    #
    ('ohm-plugins-misc', {}),

    #
    ('libicd-tor', {}),

    #
    ('tor-network-applet', {}),

    #
    ('libicd-wireguard', {}),

    #
    ('wireguard-network-applet', {}),

    #
    ('libicd-openvpn', {}),

    #
    ('openvpn-network-applet', {}),

    #
    ('wpeditor', {}),

    #
    ('calendar-ui-widgets', {}),

    #
    ('libmodest-dbus-client', {}),

    #
    ('tinymail', {}),

    #
    ('gtkhtml3', {}),

    #
    ('modest', {}),

    #
    ('glib', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('wireguard-tools', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('gnome-contacts', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('sgx-ddk-um', {
        'arches': ['armhf'],
    }),

    #
    ('maemo-kernel-config', {
        'arches': ['armhf'],
    }),

    #
    ('maemo-statusmenu-volume', {}),

    #
    ('libQuotient', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('telepathy-tank', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('linux-firmware-pine64-rtl8723-bt', {
        'arches': ['all'],
    }),

    #
    ('telepathy-gabble', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('libaccounts', {}),

    #
    ('rtcom-accounts-ui', {}),

    #
    ('rtcom-accounts-ui-client', {}),

    #
    ('rtcom-accounts-plugins', {}),

    #
    ('rtcom-presence-ui', {}),

    #
    ('cellulard', {}),

    #
    ('iphb-dkms', {
        'arches': ['all'],
    }),

    # Dep python2-gconf
    ('pycairo2', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # Dep python2-gconf
    ('pygobject2', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    ('python2-gconf', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    ('notify-python', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # elogind crap
    ('tinydm', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
        'arches': ['all'],
    }),

    #
    ('autologin', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # maemo-ringtones
    ('maemo-ringtones', {
        'host': 'https://github.com/maemo-leste-assets/%s',
        'arches': ['all'],
    }),

    ('qtwebengine', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    ('libcamera', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('firmware-ov5640', {
        'arches': ['all'],
    }),

    #
    ('slack-libpurple', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('voicecall', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # Extra pkg, dep for maemo-translate
    ('cpuinfo', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('harbour-shutter', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('pinephone-keyboard', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
        'arches': ['all'],
    }),

    #
    ('policykit-1-hildon', {}),

    #
    ('dh-python', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
        'arches': ['all'],
    }),

    #
    ('mafw-gst-renderer', {}),

    #
    ('tracker-miners', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('tracker', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('telepathy-ring', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('telepathy-haze', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('gst-plugins-base1.0', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # Extra pkg
    ('signald', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    # Extra pkg
    ('libpurple-signald', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('tdlib-purple', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
    }),

    #
    ('maemo-user-guide', {
        'arches': ['all'],
    }),

    #
    ('qxmpp', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('telepathy-nonsense', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('libomemo-c', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('olm', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    #
    ('qt-input-maemo', { }),

    # For trixie only?
    ('gconf', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s'
    }),

    # Bring dh_gconf back
    ('debhelper', {
        'host': 'https://github.com/maemo-leste-upstream-forks/%s',
        'arches': ['all'],
    }),
])
