#!/usr/bin/python3
""" fabric module """
from fabric.api import local
import time


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
