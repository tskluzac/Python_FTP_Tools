import os
import glob

outputfile = "/home/ubuntu/cdiac_scraper/ianTracker8"

#Creates header row of output csv file
with open(outputfile, 'a') as summary:
    summary.write('File Name,File Size' + '\n')

#Loop walks through all files of designated extension
#and writes new line to output csv file
for file in glob.glob(r'/home/ubuntu/ianData/*'):
    filename = os.path.basename(file)
    filesize = os.path.getsize(file)

    with open(outputfile +'.csv', 'a') as summary:
        summary.write(str(filename) + ',' +
                      str(filesize) + '\n')


# import sys,os, glob
#
# root = "/home/tskluzac/Downloads/"
# path = os.path.join(root, "targetdirectory")
#
# for path, subdirs, files in os.walk(root):
#     for name in files:
#         size = os.stat(path).st_size
#         #if size%4096 != 0:
#         print(name)
#         print(size)
#
#
#
#         print(name)
#         print os.path.join(path, name)
#         #print os.path.getsize(file)

