#!/usr/bin/python3
""" fabric module """
from os import path
from fabric.api import run, local, env, execute

#env.hosts = ['34.75.197.138', '104.196.173.55']


def clean_local_releases(nb=0):
    """ clean versions folder locally """
    mypath = 'versions'

    if int(nb) == 0:
        nb = '2'
    else:
        nb = str(int(nb) + 1)
    if path.exists(mypath) is False:
        return False

    local('find {} -type f | sort -r |  tail -n +{} | xargs rm -f'
          .format(mypath, nb))


def clean_releases_from_server(nb=0):
    """ clean /data/web_static/releases remotely """
    if int(nb) == 0:
        nb = '2'
    else:
        nb = str(int(nb) + 1)

    mypath = '/data/web_static/releases'
    if path.exists(mypath) is False:
        return False
    run(' find {}  -mindepth 1 -maxdepth 1 -type d | sort -r |  tail -n +{} | xargs rm -fr'
        .format(mypath, nb))


def do_clean(number=0):
    clean_local_releases(number)
    execute(clean_releases_from_server, nb=number,
            hosts=['34.75.197.138', '104.196.173.55'])
