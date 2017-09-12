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
        upstream-tag=%(version)s  # this is the format of the git tag where we take the actual                              # software version




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

Document job config file here, etc.
