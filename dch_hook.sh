#!/bin/bash

[ "$distribution" = jessie ] && release_num=0
[ "$distribution" = ascii ]  && release_num=1

_srcinfo=$(dpkg-parsechangelog -n 1 -l debian/changelog)
_srcname=$(echo "$_srcinfo" | grep '^Source: ' | cut -d' ' -f2)
_srcver=$(echo "$_srcinfo" | grep '^Version: ' | cut -d' ' -f2)

echo "$_srcver" | grep -q ':' - && {
        _epoch="$(echo $_srcver | awk -F':' '{print $1}')"
        _srcver="$(echo $_srcver | awk -F':' '{print $2}')"
}

_pkgname=$(grep 'Package: ' debian/control | sed 1q | cut -d' ' -f2)
_deb=$(find /srv/repository/release/$release/pool -type f -name "${_pkgname}_${_srcver}*.deb" | sed 1q)
_deb=$(basename $_deb)
echo "*** deb == $_deb ***"

_buildnum=$(echo $_deb | awk -F'+' '{print $NF}' | cut -d'_' -f1)
echo "*** buildnum == $_buildnum ***"

if echo $_buildnum | grep -q "^${release_num}m7$"; then
    echo "*** Found previous build (no rebuilds). Appending .1"
    _buildnum="${_buildnum}.1"
elif echo $_buildnum | grep -q "^${release_num}m7\.."; then
    echo "*** Found previous rebuild. Incrementing build number ***"
    _buildnum=$(echo $_buildnum | awk -F. '{print $NF}')
    _buildnum=$(expr $_buildnum + 1)
    _buildnum="${release_num}m7.${_buildnum}"
else
    echo "*** Did not find previous builds. Assuming +${release_num}m7 ***"
    _buildnum="${release_num}m7"
fi

_firstline="$(sed 1q debian/changelog)"

[ -n "$_epoch" ] && _srcver="${_epoch}:${_srcver}"

_tempchangelog=$(mktemp)
tac debian/changelog > $_tempchangelog
cat <<EOF >> $_tempchangelog

 -- Jenkins Auto Builder <spam1@wizzup.org>  $(date +'%a, %d %b %Y %H:%M:%S +0200')
 
  * Increment build number

$_srcname (${_srcver}+${_buildnum}) unstable; urgency=medium
EOF

tac $_tempchangelog > debian/changelog
rm $_tempchangelog

