import os
import glob

"""
    This local FTP scraper creates a csv-file containing filename and filesizes
      from a local directory.  User should change (1) location of output csv-file
      and (2) input-directory to be scanned-over.

    Author: Tyler J. Skluzacek, University of Chicago
    Email: skluzacek@uchicago.edu
    Github: tskluzac
    Last Edited: 11/19/2016
"""


outputfile = "/home/ubuntu/cdiac_scraper/DESTINATION"

#Creates header row of output csv file
with open(outputfile, 'a') as summary:
    summary.write('File Name,File Size' + '\n')

#Loop walks through all files of designated extension
#and writes new line to output csv file
for file in glob.glob(r'/home/ubuntu/SOURCE/*'): #Change this line to input directory. Leave '/*' for whole directory.
    filename = os.path.basename(file)
    filesize = os.path.getsize(file)

    with open(outputfile +'.csv', 'a') as summary:
        summary.write(str(filename) + ',' +
                      str(filesize) + '\n')