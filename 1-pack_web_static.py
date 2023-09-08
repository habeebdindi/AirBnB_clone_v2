#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of the AirBnB_Clone_v2 repo
"""
from fabric.operations import local
import datetime


def do_pack():
    """ Archives the web_static folder
    """
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive = local("tar -czvf versions/web_static_{}.tgz web_static"
                    .format(time))
    if archive.failed:
        return None
    else:
        return archive
