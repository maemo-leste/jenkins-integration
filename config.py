from collections import OrderedDict
import repos_core, repos_l10n, repos_extras

DEFAULT_RELEASES = {
    'leste': [
        'ascii',
        'ascii-devel',
        'beowulf',
        'beowulf-devel',
        'beowulf-experimental',
        'stretch',
        'buster',
        'chimaera',
        'chimaera-testing',
        'chimaera-devel',
        'chimaera-experimental',
        'daedalus',
        'daedalus-testing',
        'daedalus-devel',
        'daedalus-experimental',
        'excalibur',
        'excalibur-testing',
        'excalibur-devel',
        'excalibur-experimental',
    ],
    'extras': [
        'ascii',
        'beowulf',
        'beowulf-devel',
        'chimaera',
        'chimaera-testing',
        'daedalus',
        'daedalus-testing',
        'excalibur',
        'excalibur-testing',
    ],
}
DEFAULT_HOST = 'https://git.maemo.org/leste/%s'
#DEFAULT_HOST = 'https://github.com/maemo-leste/%s'
DEFAULT_ARCHES = ['amd64', 'armhf', 'arm64']
"""
# self documenting code comments
_jobs = {
    'job-name': {'repo-name': 'repo-name-if-not-equal-to-job-name',
                 'host': 'host here if not equal to DEFAULT_HOST',
                 'releases': {'maemo-leste-repo': 'devuan-distribution'}
"""

_jobs = OrderedDict()
_jobs.update(repos_core._jobs)
_jobs.update(repos_l10n._jobs)
_jobs.update(repos_extras._jobs)


def get_jobs():
    jobs = OrderedDict()
    for job, args in _jobs.items():
        repo_name = args.get('repo-name', job)
        host = args.get('host', DEFAULT_HOST) % repo_name
        releases = args.get('releases', DEFAULT_RELEASES)
        arches = args.get('arches', DEFAULT_ARCHES)

        jobs[job] = dict(repo_name=repo_name,
                         host=host,
                         releases=releases,
                         arches=arches)

    return jobs
