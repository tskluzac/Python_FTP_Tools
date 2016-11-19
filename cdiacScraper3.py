from ftplib import *
import send_to_csv
import os


"""
    This ftp_scraper will create a path-directory of all files and filesizes in given FTP server.
    Code can be uncommented to (1) do in a single recursive swath, and (2) actually download files
    a local machine.

    Author: Tyler J. Skluzacek, University of Chicago
    Email: skluzacek@uchicago.edu
    Github: tskluzac
    Last Edited: 11/18/2016
"""


path_size_holder = [('Path', 'Size')]


def _is_ftp_dir(ftp_handle, name, guess_by_extension=True):
    ### Test: Is Directory?
    # If name has a '.' in 3rd or 4th from last position (.csv/.nc), then probably a file!
    # This allows us to skip the SLOW '.cwd()' command over and over and over...

    if guess_by_extension is True:
        if (name[-4] == '.') or (name[-3] == '.'):
            return False

    original_cwd = ftp_handle.pwd()     # remember the current working directory
    try:
        ftp_handle.cwd(name)            # try to set directory to new name
        ftp_handle.cwd(original_cwd)    # set it back to what it was
        return True
    except:
        return False


def _make_parent_dir(fpath):
    print("Initializing: Checking parent-child/directory-subdirectory relationship...")
    """ Does path (given a file) actually exist? """
    dirname = os.path.dirname(fpath)
    while not os.path.exists(dirname):
        print("Doing A-b")
        try:
            os.mkdir(dirname)
            print("created {0}".format(dirname))
        except:
            _make_parent_dir(dirname)



"""Unpack each file's size. Can UNcomment Part B to download it"""
def _download_ftp_file(ftp_handle, name, dest, overwrite):
    try:
        size = ftp.size(name)
        path_size_tuple = (name, size)
        path_size_holder.append(path_size_tuple)
        print("Recording: " + name)

    ### If there is no name or filesize (skip it)
    except:
        pass

    ### PART B ###
    # """ downloads a single file from an ftp server """
    # _make_parent_dir(dest)
    # if not os.path.exists(dest) or overwrite is True:
    #     with open(dest, 'wb') as f:
    #         ftp_handle.retrbinary("RETR {0}".format(name), f.write)
    #     print("downloaded: {0}".format(dest))
    # else:
    #     print("already exists: {0}".format(dest))


def _mirror_ftp_dir(ftp_handle, name, overwrite, guess_by_extension):
    print("Opening directory: " + name)
    """ replicates a directory on an ftp server recursively """
    for item in ftp_handle.nlst(name):
        if _is_ftp_dir(ftp_handle, item):
            _mirror_ftp_dir(ftp_handle, item, overwrite, guess_by_extension)
        else:
            _download_ftp_file(ftp_handle, item, item, overwrite)


def download_ftp_tree(ftp_handle, path, destination, overwrite=False, guess_by_extension=True):
    """
    Downloads an entire directory tree from an ftp server to the local destination

    :param ftp_handle: an authenticated ftplib.FTP instance
    :param path: the folder on the ftp server to download
    :param destination: the local directory to store the copied folder
    :param overwrite: set to True to force re-download of all files, even if they appear to exist already
    :param guess_by_extension: It takes a while to explicitly check if every item is a directory or a file.
        if this flag is set to True, it will assume any file ending with a three character extension ".???" is
        a file and not a directory. Set to False if some folders may have a "." in their names -4th position.
    """
    os.chdir(destination)
    _mirror_ftp_dir(ftp_handle, path, overwrite, guess_by_extension)
    send_to_csv.writer(path_size_holder)


#### USAGE HERE ####
host ="cdiac.ornl.gov"
user = ""
password = ""

print("Connecting to {}".format(host))
ftp = FTP(host) ### connect to FTP
ftp.login()

print("Logged in :)")


### USE THIS IF YOU HAVE STRONG RECURSION DEPTH.
### In format download_ftp_tree(ftp-server-host, path_to_parent, path_to_local_destination(for downloads))
#download_ftp_tree(ftp,'/pub/' , '/home/tskluzac/Downloads/')


### Broken into bits::: For local machines with weak recursive depths (<1500ish)
### Don't run the previous one unless you are for-certain using a muscular computer.

download_ftp_tree(ftp,'/pub2/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub3/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub4/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub5/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub6/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub7/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub8/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub9/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub10/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub11/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub12/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/incoming/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/key/' , '/home/tskluzac/Downloads/')
download_ftp_tree(ftp,'/pub/' , '/home/tskluzac/Downloads/')


#print(path_size_holder)


