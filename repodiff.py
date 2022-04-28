#!/usr/bin/env python3
import sys
from subprocess import check_output
from os.path import join
from argparse import ArgumentParser

from debian.debian_support import Version

REPO_BASE = '/srv/repository/leste'

# Tool to help answer questions:
# * What packages need to be moved from devel to stable (show version diff)
# * What packages are in devel that are not in stable?
# * What packages can we remove from devel because they are in stable?


def parse_packages(output):
    res = {}

    for line in output.split('\n'):
        if not line.strip():
            continue

        idx = line.find('|')
        repo = line[:idx]
        line = line[idx + 1:]

        idx = line.find('|')
        section = line[:idx]
        line = line[idx + 1:]

        idx = line.find(':')
        archsrc = line[:idx]
        line = line[idx + 1:]

        line = line.strip()

        idx = line.find(' ')
        pkgname = line[:idx]
        line = line[idx + 1:]

        version = line

        index = (section, pkgname)
        #index = (section, archsrc, pkgname)

        res[index] = (repo, version, archsrc)

    return res


def get_source_pkg(index, ver):
    p = join(REPO_BASE, 'log')
    matches = check_output(['grep', '-Erl', 'Binary:.*%s' % index[1], p]).decode('utf-8')
    for line in matches.split('\n'):
        print(line)


if __name__ == '__main__':
    parser = ArgumentParser(description='repodiff')
    parser.add_argument('-f', '--filter-type', default=None, choices=['source',])
    parser.add_argument('-t', '--task', required=True, choices=['missing', 'newer', 'deprecated'])

    parser.add_argument('reference_repo', metavar='N', type=str)
    parser.add_argument('compare_repo', metavar='N', type=str)

    args = parser.parse_args()

    category_left = args.reference_repo
    category_right = args.compare_repo
    task = args.task

    pkg_left = parse_packages(check_output(['reprepro', '-b', REPO_BASE, 'list', category_left]).decode('utf-8'))
    pkg_right = parse_packages(check_output(['reprepro', '-b', REPO_BASE, 'list', category_right]).decode('utf-8'))

    if task == 'missing':
        print('Packages in %s but not in %s' % (category_left, category_right))
        for index, ver in pkg_left.items():
            if args.filter_type is not None and ver[2] != args.filter_type:
                continue

            if index not in pkg_right:
                #get_source_pkg(index, ver)
                print(index[1], ver[1], ver[2])
                continue


    if task == 'newer':
        print('Packages in %s that are newer than %s' % (category_left, category_right))
        for index, ver in pkg_left.items():
            if args.filter_type is not None and ver[2] != args.filter_type:
                continue

            if index not in pkg_right:
                continue

            _, left_ver, _ = pkg_left[index]
            _, right_ver, _ = pkg_right[index]

            left_ver_d = Version(left_ver)
            right_ver_d = Version(right_ver)

            if left_ver_d > right_ver_d:
                print(index[1], left_ver, '(>', right_ver, ')')

    if task == 'deprecated':
        print('Packages in %s that are older than %s' % (category_left, category_right))
        for index, ver in pkg_left.items():
            if args.filter_type is not None and ver[2] != args.filter_type:
                continue

            if index not in pkg_right:
                continue

            _, left_ver, _ = pkg_left[index]
            _, right_ver, _ = pkg_right[index]

            left_ver_d = Version(left_ver)
            right_ver_d = Version(right_ver)

            if left_ver_d < right_ver_d:
                print(index[1], left_ver, '(>', right_ver, ')')
