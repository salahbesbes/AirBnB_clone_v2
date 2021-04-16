#!/usr/bin/python3
""" fabric module """
from fabric.api import *
import re

env.user = 'ubuntu'
env.hosts = ['34.75.197.138', '104.196.173.55']


def do_deploy(archive_path):
    """ Deploy archive

    Args:
        archive_path ([string]): [path to the archive]
    """
    if not archive_path:
        return False

    else:
        pattern = r'web_static_+\d+\.tgz$'
        try:
            archive_name = re.search(pattern, archive_path).group()
            archive = archive_name.split('.')[0]
            archive_destination = '/data/web_static/releases/{}'.format(
                archive)
            put(archive_path, '/tmp')
            run('mkdir -p {dest} '.format(dest=archive_destination))
            run('tar -xzf /tmp/{ar_name} -C {dest} '
                .format(ar_name=archive_name, dest=archive_destination))
            run('rm -f /tmp/{ar_name} '.format(ar_name=archive_name))
            run('mv /data/web_static/releases/{archive}/web_static/* \
                /data/web_static/releases/{archive}/'
                .format(archive=archive))
            run('rm -rf /data/web_static/releases/\
                {archive}/web_static'.format(archive=archive))
            run('rm -rf /data/web_static/current ')
            run('ln -sf /data/web_static/releases/{archive}\
                /data/web_static/current'
                .format(archive=archive))
            return True

        except Exception:
            return False
