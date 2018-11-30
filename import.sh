#!/bin/sh
#
# Imports the -all debs into a given repository.

repopath="/srv/repository/release"
debpaths="$repopath/leste"

case "$1" in

	leste-devel|bayamo)

		find "$debpaths" -type f -name '*l10n*.deb' | \
			xargs reprepro -b "$repopath/$1" includedeb "$1" || exit 1

		find "$debpaths" -type f -name '*theme*.deb' | grep -v cacher | \
			xargs reprepro -b "$repopath/$1" includedeb "$1" || exit 1
		;;

	*)
		echo "No existing repo for $1. Create it before importing."
		exit 1
		;;
esac
