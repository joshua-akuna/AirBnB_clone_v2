#!/usr/bin/python3
""" The module implements the do_pack function """
from datetime import datetime
from fabric.api import *
from os.path import exists
import os
import paramiko


env.hosts = ["100.25.24.43", "100.24.253.164"]
env.user = "ubuntu"
# env.key_filename = "~/.ssh/school"
# env.use_ssh_config = True


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
    try:
        if not exists(archive_path):
            return False

        # upload the archive to the /tmp/ directory of the remote servers
        put(archive_path, "/tmp/")
        # Creating path variables for the remote servers
        archive_name = archive_path.split('/')[-1]
        uncompressed_path = "/data/web_static/releases/{}/".format(
                archive_name.split('.')[0])

        # making directory, where the archive contents will be extracted to
        run('sudo mkdir -p {}'.format(uncompressed_path))
        # Extracting archive to specified location
        run('sudo tar -xzf /tmp/{} -C {}'.format(
            archive_name, uncompressed_path))

        # deleting archive file
        run('sudo rm /tmp/{}'.format(archive_name))

        # moving all files in the extracted archive directory to the parent
        run('sudo mv {}web_static/* {}'.format(
            uncompressed_path, uncompressed_path))

        # deleting the extracted archive directory
        run('sudo rm -rf {}web_static'.format(uncompressed_path))

        # deleting and recreating the symlink
        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s {} /data/web_static/current'.format(uncompressed_path))

        print('New version deployed!')

        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """creates and distributes an archive to the web server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """deletes all unnecessary archives in the local versions directory and
        in the remote /data/web_static/releases directory of the web servers
    """
    num = int(number)
    if num == 0:
        num = 1

    local_archives = sorted(os.listdir("versions"))
    # print(local_archives)
    for archive in local_archives[:-num]:
        local("rm -f versions/{}".format(archive))

    remote_archives = run("ls -1 /data/web_static/releases").split()
    # print(remote_archives)
    for archive in remote_archives[:-num]:
        run("sudo rm -rf /data/web_static/releases/{}".format(archive))
