#!/usr/bin/python3
""" The module implements the do_pack function """
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """ The function generates a .tgz archive from the contents
        of the web_static folder of the AirBnB Clone repo
    """
    try:
        # Creates a name for each archive
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Creates a directory named version if it does not exists
        local("mkdir -p versions")

        # Archives the contents of the web_static directory
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
