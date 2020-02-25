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

This document describes the (auto) build setup for maemo-on-devuan.
Jenkins is used, together with `jenkins-debian-glue`, and a set of custom scripts

This document hopefully helps those seeking to either help our maemo-on-devuan
by adding more repositories and packages, or those who want to set up similar
infrastructure.


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

1. Add `maemo/RELEASE` branch (where `RELEASE` is `ascii`, `ascii-devel`,
   `beowulf`) that contains the `debian/` directory
2. Ensure debian/control follows recent practices (if not, you'll find out
   during build)
3. Add debian/gbp.conf

    .. code-block:: ini

        [DEFAULT]
        # this is the format of the git tag where we take the actual software version
        upstream-tag=%(version)s

4. To build a package, please see `Making a release of a package in the repository`_


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
3. To actually get Jenkins to build the package, read
   `Jenkins job management`_, and specifically `Defining jobs`.


Versioning
==========

Once we reach an agreement on the exact version strings, document that here.


Jenkins job management
======================

All jenkins jobs descent (are copies of) the following three jobs:

1. `jenkins-debian-glue-source`
2. `jenkins-debian-glue-binaries`
3. `jenkins-debian-glue-repos`

The `jenkins-debian-glue-source` job will fetch any new sources and trigger a
`jenkins-debian-glue-binaries` job. The `jenkins-debian-glue-binaries` job will
build packages on the machines labeled with the respective architecture. Finally,
`jenkins-debian-glue-repos` will copy all artifacts to the master node and
update the repository with packages.

Section `Defining jobs` documents how to add a job to the currently existing
set of jobs. This should be all that is required to start building a package,
given that it's dependencies are present.

.. These can be passed as params to build_job().
..  build_job(name, parameters=None, token=None)
..     parameters – parameters for job, or None, dict



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
        # 'host': required if host is not https://github.com/maemo-leste/%s
        # 'releases': {'leste': 'ascii', 'extras': 'beowulf'}
        'libcal': {'repo-name': 'libcal'}
    }


Slave nodes
-----------

https://jenkins-debian-glue.org/faq/#slave_nodes

For slave nodes, we install the system the same way we did with the master
node. However, Jenkins does not have to be running on the slave node. Our
master node will handle this when we introduce the node to it. The only thing
that matters is having an accessible ssh port and ssh keys setup between the
two jenkins accounts (master - slave).

We can add a slave node using the HTTP interface of the master node.

1. Manage Jenkins
2. Manage Nodes
3. New node

On the `New node` screen, we have to configure our slave node:

    * `Node name` should be the architecture we are building for.
    * Set `Permanent Agent`

Once this is set, proceed with configuring as follows:

    * Name: `armel`
    * Description: `armv7 machine`
    * # of executors: `2`
    * Remote root directory: `/var/lib/jenkins`
      (this is ~jenkins on master)
    * Labels: `armel`
    * Usage: `Only build jobs with label expressions matching this node`
    * Launch method: `Launch slave agents via SSH`
    * Host: `armelslave.maemo.org`
    * Credentials: setup proper credentials here
    * Host key verification strategy: `Known hosts file`
      (this requires a manual login once beforehand)
    * Port: `22` (or whatever is set up on the slave)

Click Save, and this should setup the node.

Since we have two nodes now, this means the master node needs to be correctly
labeled as well. Simply go to the configuration menu in the UI and add a label
to the master node matching the architecture that will be built using the
master node. In our case this is `amd64`.


Scoping of slave nodes on the master node repository
----------------------------------------------------

Make sure you add the new architecture to the reprepro configuration(s) where
they are located on the master node. In our case this is `/srv/repository/conf`
and `/srv/repository/release/leste/conf`.


Miscellaneous
=============


dch_hook
--------

The `dch_hook.sh` file is a shell script containing our custom versioning
logic. It's defined in our `sources.xml` template, and executed at some
point in the process of `generate-git-snapshot`. For it to work as we have
intended, some changes are required in `/etc/jenkins/debian_glue`:

    .. code-block:: sh

        USE_ORIG_VERSION=true
        SKIP_DCH=true
        UNRELEASED_APPEND_COMMIT=false

The concept of this hook is that all our built packages will have a maemo
version appended on the end of the filename and in the changelog. With this
we avoid polluting the git repo, but it still allows us to see how many builds
have been triggered for a specific package.

Let's take libcal as an example. In git, our changelog has the version of
`0.3-2`. When the source job is built, `generate-git-snapshot` combined with
`dch-hook.sh` will append `+0m7` to it for the initial build. This results
in the actual package version being `0.3-2+0m7`. If we rebuild this package
without bumping the version in git, the following build will have `+0m7.1`
appended. Each subsequent build will increment the latter `.1` by one, until
the version in git is changed. It will then reset back to `+0m7` and repeat
the process.
