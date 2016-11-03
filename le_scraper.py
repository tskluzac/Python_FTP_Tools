from ftplib import FTP
import os, sys, os.path
import quickstart


#### GET ALL FROM ALL SUBDIRECTORIES #####
from ftplib import FTP
from socket import *


def get_dirs_ftp(folder=""):
    try:
        contents = ftp.nlst(folder)
        folders = []
        for item in contents:
            if "." not in item:
                folders.append(item)
                quickstart.extract(item, ftp)
        return folders
    except timeout:
        print("Caught Timeout. Type 1.")





def get_all_dirs_ftp(folder=""):
    try:
        dirs = []
        new_dirs = []

        new_dirs = get_dirs_ftp(folder)

        cats = 0
        while (len(new_dirs) > 0) and (cats<10):
                for dir in new_dirs:
                    dirs.append(dir)
                old_dirs = new_dirs[:]
                new_dirs = []
                for dir in old_dirs:
                    for new_dir in get_dirs_ftp(dir):
                        new_dirs.append(new_dir)
                        cats += 1
                        print("meow")


        dirs.sort()
        return dirs

    except timeout:
        print("Caught Timeout. Type 2.")


host ="cdiac.ornl.gov"
user = ""
password = ""

print("Connecting to {}".format(host))
ftp = FTP(host) ### connect to FTP
ftp.login()
ftp.cwd('/pub') ### Limit FTP path to /pub

print("Connected to {}".format(host))

print("Getting directory listing from {}".format(host))
all_dirs = get_all_dirs_ftp()
print("***PRINTING ALL DIRECTORIES***")
for dir in all_dirs:
    print(dir)




def extract(directory):

    exit()