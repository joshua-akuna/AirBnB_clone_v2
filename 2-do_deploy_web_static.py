#!/usr/bin/python3
""" The module implements the do_pack function """
from datetime import datetime
from fabric.api import *
from os.path import exists


env.hosts = ["100.25.24.43", "100.24.253.164"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


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


def do_deploy(archive_path):
    """ distributes an archive to my web servers """
    if exists(archive_path):
        put(archive_path, "/tmp/")
        archive_name = archive_path.split('/')[-1]
        uncompressed_path = "/data/web_static/releases/{}/".format(
                archive_name.split('.')[0])
        print(uncompressed_path)

        run('sudo mkdir -p {}'.format(uncompressed_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(
            archive_name, uncompressed_path))

        run('sudo rm /tmp/{}'.format(archive_name))

        run('sudo mv {}web_static/* {}'.format(
            uncompressed_path, uncompressed_path))

        run('sudo rm -rf {}web_static'.format(uncompressed_path))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s {} /data/web_static/current'.format(uncompressed_path))

        print('New version deployed!')

        return True
    else:
        return False
