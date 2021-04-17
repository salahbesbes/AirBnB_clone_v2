#!/usr/bin/python3
""" fabric module """
from fabric.api import *
import re
import time
from os import path


# env.user = 'ubuntu'


def do_pack():
    """Make a tar.gz archive of da (/web_static )."""
    try:
        name_folder = "web_static"
        archive_name = "{}_{}.tgz".format(name_folder, time.strftime(
            "%Y%m%d%H%M%S", time.gmtime()))
        path_archive = './versions/{}'.format(archive_name)
        local("mkdir -p versions; \
                tar -zvcf {} {}".format(path_archive, name_folder))
        return path_archive
    except Exception:
        return None


def do_deploy(archive_path):
    """ Deploy archive
        line to call: fab -f 2-do_deploy_web_static.py do_deploy:archive_path=\
            versions/web_static_20170315003959.tgz -u ubuntu
    Args:
        archive_path ([string]): [path to the archive]
    """
    if path.exists(archive_path) is False:
        return False
    pattern = r'web_static_+\d+\.tgz$'
    archive_name = re.search(pattern, archive_path).group()
    archive = archive_name.split('.')[0]
    release = '/data/web_static/releases'
    archive_destination = '/data/web_static/releases/{archive}/'.format(
        archive=archive)
    put(archive_path, '/tmp')
    run('rm -fr {release}/{archive}/'
        .format(release=release, archive=archive))
    run('mkdir -p {dest} '.format(dest=archive_destination))
    run('tar -xzf /tmp/{ar_name} -C {dest}'
        .format(ar_name=archive_name, dest=archive_destination))
    run('rm /tmp/{ar_name} '.format(ar_name=archive_name))

    run('mv {release}/{archive}/web_static/* {release}/{archive}/'
        .format(release=release, archive=archive))

    run('rm -rf {release}/{archive}/web_static'
        .format(release=release, archive=archive))
    run('rm -rf /data/web_static/current')
    run('ln -fs {release}/{archive}/ /data/web_static/current'
        .format(release=release, archive=archive))
    return True


def deploy():
    """     full deploy: creates and distributes an archive to a web servers,
    """

    # result = execute(functionName, x=5, y=10, hosts=['host-1', 'host-2'])
    # print(result) #    {'host-1': 15, 'host-2': 15}
    arch_path = do_pack()

    if not arch_path:
        return False
    return execute(do_deploy, archive_path=arch_path,
                   hosts=['34.75.197.138', '104.196.173.55'])
