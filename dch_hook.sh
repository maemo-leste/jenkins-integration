#!/bin/bash
_srcinfo=$(dpkg-parsechangelog -n 1 -l debian/changelog)
_srcname=$(echo "$_srcinfo" | grep '^Source: ' | cut -d' ' -f2)
_srcver=$(echo "$_srcinfo" | grep '^Version: ' | cut -d' ' -f2)

_pkgname=$(grep 'Package: ' debian/control | sed 1q | cut -d' ' -f2)
_deb=$(find /srv/repository/release/$release/pool -type f -name "${_pkgname}_${_srcver}*.deb" | sed 1q)
_deb=$(basename $_deb)
echo "*** deb == $_deb ***"

_buildnum=$(echo $_deb | awk -F'+' '{print $NF}' | cut -d'_' -f1)
echo "*** buildnum == $_buildnum ***"

if echo $_buildnum | grep -q '^.m7$'; then
    echo "*** Found previous build. Incrementing build number ***"
    _buildnum=$(echo $_buildnum | cut -c1)
    _buildnum=$(echo "$_buildnum + 1" | bc)
    _buildnum="${_buildnum}m7"
else
    echo "*** Did not find previous builds. Assuming +0m7 ***"
    _buildnum="0m7"
fi

_firstline="$(sed 1q debian/changelog)"

_tempchangelog=$(mktemp)
tac debian/changelog > $_tempchangelog
cat <<EOF >> $_tempchangelog

 -- Jenkins Auto Builder <spam1@wizzup.org>  $(date +'%a, %d %b %Y %H:%M:%S +0200')
 
  * Increment build number

$_srcname (${_srcver}+${_buildnum}) unstable; urgency=medium
EOF

tac $_tempchangelog > debian/changelog
rm $_tempchangelog

