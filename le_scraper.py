# import httplib2
# from BeautifulSoup import BeautifulSoup, SoupStrainer
#
# http = httplib2.Http()
# status, response = http.request('http://www.nytimes.com')
#
# for link in BeautifulSoup(response, parseOnlyThese = SoupStrainer('a')):
#     if link.has_attr('href'):
#         print link['href']

# import urllib
# import lxml.html
#
# connection = urllib.urlopen('ftp://cdiac.ornl.gov/pub')
#
#
# dom = lxml.html.fromstring(connection.read())
#
#
# for link in dom.xpath('//a/@href'):
#     print(link)

from ftplib import FTP
import os, sys, os.path

#ianData
# ddir = '/home/tyler/ianData/'
# os.chdir(ddir)
# ftp = FTP('cdiac.ornl.gov')
# ftp.login()
# ftp.cwd('/pub')
#
# filenames = ftp.nlst()
# print filenames
#
# for filename in filenames:
#     local_filename = os.path.join('/ianData/', filename)
#     file = open(local_filename, 'wb')
#     ftp.retrbinary('RETR ' + filename, file.write)
#
#     file.close()
#ftp.quit()

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
        return folders
    except timeout:
        print("Caught a timeout, type 1")



def get_all_dirs_ftp(folder=""):
    try:
        dirs = []
        new_dirs = []

        new_dirs = get_dirs_ftp(folder)

        while len(new_dirs) > 0:
            for dir in new_dirs:
                dirs.append(dir)

            old_dirs = new_dirs[:]
            new_dirs = []
            for dir in old_dirs:
                for new_dir in get_dirs_ftp(dir):
                    new_dirs.append(new_dir)

        dirs.sort()
        return dirs

    except timeout:
        print("caught timeout, type 2")


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


