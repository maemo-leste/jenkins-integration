===================================
Jenkins automated builds <NAMEHERE>
===================================

.. |date| date:: %Y-%m-%d %H:%M

:Date: |date|
:Version: 0.1
:Status: Work in progress

.. contents::



Introduction
============





Repository management
=====================

All repositories currently exist on (git.devuan.org/maemo|github.com/fremantle-gtk2 -
pick one).  If the source for a package does not yet exist, please create such
a repository on the right git host.

There are various different cases when one wants to add dependencies / import packages:

1. Source exists for the package, and it's already available and prepared (e.g. anything on github.com/fremantle-gtk2)
2. Source exists but it's not yet available/packaged in a sensible place for us
3. Only a .deb exists, but the package is source only
4. Only a .deb exists, but it contains binaries and no source code is available.

In cases 1-3, you should be able to import a package with relative ease. In the
last case (4), we need to reverse engineer the package before we attempt to
import it.

The repository name does not have to correspond to the exact package name, as
the package names are described in the `debian/` directory instead. 


Adding a repository
-------------------

Steps:

1. Add `maemo/RELEASE` branch (where `RELEASE` is `jessie`, `ascii`,
   `unstable`) that contains the `debian/` directory
2. Ensure debian/control follows recent practices (if not, you'll find out
   during build)
3. Add debian/gbp.conf

    .. code-block:: ini

        [DEFAULT]
        debian-branch=master  # the debian-branch is the branch the sources are taken from
        upstream-tag=%(version)s  # this is the format of the git tag where we take the actual software version




Making a release of a package in the repository
-----------------------------------------------

Jenkins will always fetch the latest `maemo/<release name>` branch, read
`debian/gbp.conf` and the `debian/changelog` file. It will pick the latest
version from the `debian/changelog`, and determine what tag to load the code
from, based on the `upstream-tag` provided above in `debian/gbp.conf`. The
source code branch needs to be tagged with such tags.


1. Add a tag to the branch we want to take the source code from. The tag should
   match the version in the `debian/changelog`.
2. Add a new `debian/changelog` entry if needed.
   Make sure the version you're adding has a proper tag in the git log.


Versioning
==========

Once we reach an agreement on the exact version strings, document that here.

Jenkins job management
======================

All jenkins jobs descent (are copies of) the following two jobs:

1. `jenkins-debian-glue-source`
2. `jenkins-debian-glue-binaries`

The `jenkins-debian-glue-source` job will fetch any new sources and trigger a
`jenkins-debian-glue-binaries` job. The `jenkins-debian-glue-binaries` job will
build packages and update the repository with packages


TODO:

* Cover how to specify what release to build for (kawai, etc)
* Cover how to specify what debian release we want to use (jessie, etc)

These can be passed as params to build_job().
 build_job(name, parameters=None, token=None)
    parameters – parameters for job, or None, dict




Defining jobs
-------------

Currently the jobs are all described in a python config file.

The job name does not have to correspond to the exact package name, as
the package names are described in the `debian/` directory instead. 

config.py

.. code-block:: python

	_jobs = {
        # job name is key, values can be:
        # 'repo-name': required if repo name is not the same as job name
        # 'host': required if host is not git.devuan.org/maemo
        # 'releases': {'kawai': 'jessie', 'unstable': 'unstable'}
        'libcal': {'repo-name': 'libcal'}
	}

