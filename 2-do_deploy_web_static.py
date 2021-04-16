#!/usr/bin/python3
""" fabric module """
from fabric.api import run, env, put
from os import path

env.hosts = ['34.75.197.138', '104.196.173.55']


def do_deploy(archive_path):
    """ Deploy archive

    Args:
        archive_path ([string]): [path to the archive]
    """
    if path.exists(archive_path) is False:
        return False
    # pattern = r'web_static_+\d+\.tgz$'
    # archive_name = re.search(pattern, archive_path).group()
    archive_name = archive_path.split('/')[1]
    archive = archive_name.split('.')[0]
    release = '/data/web_static/releases'
    archive_destination = '/data/web_static/releases/{archive}/'.format(
        archive=archive)
    put(archive_path, '/tmp')
    run('mkdir -p {dest} '.format(dest=archive_destination))
    run('tar -xzf /tmp/{ar_name} -C {dest}'
        .format(ar_name=archive_name, dest=archive_destination))
    run('rm /tmp/{ar_name} '.format(ar_name=archive_name))

    run('mv {release}/{archive}/web_static/* {release}/{archive}/'
        .format(release=release, archive=archive))

    run('rm -rf {release}/{archive}/web_static'
        .format(release=release, archive=archive))
    run('rm -rf /data/web_static/current')
    run('ln -s {release}/{archive}/data/web_static/current'
        .format(release=release, archive=archive))
    return True
