from collections import OrderedDict
"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'maemo-leste-repo': 'devuan-distribution'}
"""

_jobs = OrderedDict([
    # l10n pkg
    ('as-config-applet-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('calendar-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-application-manager-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-common-strings-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-control-panel-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-control-panel-personalisation-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-fm-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-input-method-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-libs-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('hildon-status-bar-usb-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('ke-recv-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('libsignonui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('maemo-af-desktop-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('maesync-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('mediaplayer-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('modest-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('modest-nokiamessaging-plugin-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-addressbook-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-accounts-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-certman-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-device-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-memory-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-screencalibration-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-applet-textinput-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-backup-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-browser-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-calculator-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-camera-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-cities-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-clock-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-connectivity-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-countries-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-display-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-dsm-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-filemanager-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-fm-transmitter-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-games-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-imageviewer-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-location-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-notes-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-pdf-viewer-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-powerup-shutdown-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-profiles-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-rss-feed-reader-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-sharing-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-sketch-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-statusbar-presence-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-statusbar-sound-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-suw-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-system-lock-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-tutorial-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-tv-out-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('osso-uri-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('policy-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('rtcom-call-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),

    # l10n pkg
    ('rtcom-messaging-ui-l10n', {
        'host': 'https://github.com/maemo-leste-translations/%s',
    }),
])
