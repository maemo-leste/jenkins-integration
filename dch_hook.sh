#!/bin/bash -x

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

_srcinfo="$(dpkg-parsechangelog -n 1 -l debian/changelog)"
_srcname="$(echo "$_srcinfo" | awk '/^Source: / {print $2}')"
_srcver="$(echo "$_srcinfo" | awk '/^Version: / {print $2}')"
_pkgname=$(grep 'Package: ' debian/control | sed 1q | cut -d' ' -f2)

# This should find the highest version (increment) of the wanted package.
_deb=$(find /srv/repository/leste/pool /srv/repository/extras/pool -type f \
           -name "${_pkgname}_${_srcver#*:}+${release_num}m7*.deb" | sort -rV | sed 1q)

if [ -n "$_deb" ] ; then
    _buildnum=$(basename $_deb | perl -pe 's,^.*\+(.*)_.*$,\1,')

    echo "*** buildnum == $_buildnum ***"

    if [ "$_buildnum" = "${release_num}m7" ]; then
        echo "*** Found previous build (no rebuilds). Appending .1"
        _buildnum="${_buildnum}.1"
    elif echo $_buildnum | grep -q "^${release_num}m7\.."; then
        echo "*** Found previous rebuild. Incrementing build number ***"
        _buildnum=$(echo $_buildnum | perl -pe 's,(?<=\.)(\d+),$1+1,e')
    else
        echo "*** Did not find previous builds. Assuming +${release_num}m7 ***"
        _buildnum="${release_num}m7"
    fi
else
    echo "*** Did not find previous builds. Assuming +${release_num}m7 ***"
    _buildnum="${release_num}m7"
fi

_tempchangelog=$(mktemp)
cat << EOF | tee $_tempchangelog
$_srcname (${_srcver}+${_buildnum}) unstable; urgency=medium

  * Increment build number

 -- Jenkins Auto Builder <spam1@wizzup.org>  $(date -R)

EOF
cat debian/changelog >> $_tempchangelog

cat $_tempchangelog > debian/changelog
rm -f $_tempchangelog
