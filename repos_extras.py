from collections import OrderedDict
"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'maemo-leste-repo': 'devuan-distribution'}
"""

_jobs = OrderedDict([
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

    # Extra pkg
    ('Trojita', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('sync-time-now-widget', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('gpsrecorder', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('qshot', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('braek', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('modrana', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('gpxsee', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),

    # Extra pkg
    ('wifi-switcher', {
        'host': 'https://github.com/maemo-leste-extras/%s',
    }),
])
