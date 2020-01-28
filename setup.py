#!/usr/bin/env python3
import subprocess
import argparse
from yaml import safe_load
from typing import *


def invokeApt(packages: List):
    try:
        for package in packages:
            subprocess.run(['sudo', 'apt', 'install', package, '-y'])
    except:
        raise OSError


def addPPA(packages: List):
    """
    Packages: list of PPA repos to be installed

    need more PPA's to reference to see whether should pexpect here instead of subprocess
    dont call this method for time being all methods that require a PPA should be install manually
    """
    try:
        for package in packages:
            subprocess.run(['sudo', 'apt-add-repository', 'ppa:{}'.format(package)])
        subprocess.run(['sudo', 'apt', 'update', '-y'])
    except:
        raise OSError


def invokeSnap(packages: List):
    try:
        for package in packages:
            subprocess.run(['sudo', 'snap', 'install', package,])
    except:
        raise OSError


def installer():
    parser = argparse.ArgumentParser(description='parses for what types of packages to install')
    parser.add_argument('-s', '--snap', action="store_true", help='enable installation of snap packages')
    parser.add_argument('-a', '--apt', action="store_true", help='enable installation of apt packages')
    args = parser.parse_args()
    try:
        with open('./packages.yaml') as yaml:
            temp = safe_load(yaml)

            if args.snap:
                invokeSnap(temp['snap'])

            if args.apt:
                invokeApt(temp['apt'])



    except OSError:
        return 50


def main():
    print('Have you enabled passwordless sudo yet. (this script requires sudo)')

    answer = input('[y]es [n]o: ')

    if answer == 'n':
        print('exiting')
        return 0

    if answer == 'y':
        installer()
        return 0

    print('unknown input exiting...')
    return 1


if __name__ == '__main__':
    main()
