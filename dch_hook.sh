#!/bin/bash

case "$distribution" in
    jessie*)
        release_num=0
        ;;
    ascii*|stretch*)
        release_num=1
        ;;
    beowulf*|buster*)
        release_num=2
        ;;
    bullseye*)
        release_num=3
        ;;
    bookworm*)
        release_num=4
        ;;
esac

_srcinfo=$(dpkg-parsechangelog -n 1 -l debian/changelog)
_srcname=$(echo "$_srcinfo" | grep '^Source: ' | cut -d' ' -f2)
_srcver=$(echo "$_srcinfo" | grep '^Version: ' | cut -d' ' -f2)

if echo "$_srcver" | grep -q ':'; then
    _epoch="$(echo $_srcver | awk -F: '{print $1}')"
    _srcver="$(echo $_srcver | awk -F: '{print $2}')"
fi

_pkgname=$(grep 'Package: ' debian/control | sed 1q | cut -d' ' -f2)
_deb=$(find /srv/repository/release/$release/pool -type f -name "${_pkgname}_${_srcver}*.deb" | sort -rg | sed 1q)

if [ -n "$_deb" ] ; then
    _deb=$(basename $_deb)
    _buildnum=$(echo $_deb | awk -F'+' '{print $NF}' | cut -d'_' -f1)

    echo "*** deb == $_deb ***"
    echo "*** buildnum == $_buildnum ***"

    if echo $_buildnum | grep -q "^${release_num}m7$"; then
        echo "*** Found previous build (no rebuilds). Appending .1"
        _buildnum="${_buildnum}.1"
    elif echo $_buildnum | grep -q "^${release_num}m7\.."; then
        echo "*** Found previous rebuild. Incrementing build number ***"
        _buildnum=$(echo $_buildnum | awk -F. '{print $NF}')
        _buildnum="${release_num}m7.$[_buildnum + 1]"
    else
        echo "*** Did not find previous builds. Assuming +${release_num}m7 ***"
        _buildnum="${release_num}m7"
    fi
else
    echo "*** Did not find previous builds. Assuming +${release_num}m7 ***"
    _buildnum="${release_num}m7"
fi

[ -n "$_epoch" ] && _srcver="${_epoch}:${_srcver}"

_tempchangelog=$(mktemp)
cat << EOF > $_tempchangelog
$_srcname (${_srcver}+${_buildnum}) unstable; urgency=medium

  * Increment build number

 -- Jenkins Auto Builder <spam1@wizzup.org>  $(date -R)

EOF
cat debian/changelog >> $_tempchangelog

cat $_tempchangelog > debian/changelog
rm -f $_tempchangelog
