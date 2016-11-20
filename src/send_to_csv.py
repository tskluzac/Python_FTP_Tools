import os
import glob
import random


def  writer(filepath_size_array, path):

    outputfile = "/home/tskluzac/PycharmProjects/CDIAC_scraper/cdiac_site_"

    path = path.replace("/","")

    with open(outputfile, 'a') as summary:
        summary.write(str("File Path") + ',' + str("FileSize") + '\n')

        for item in filepath_size_array:
            filename = item[0]
            print(filename)
            filesize = item[1]
            print(filesize)

            with open(outputfile + path + '.csv', 'a') as summary:
                summary.write(str(filename) + ',' +
                          str(filesize) + '\n')

    print("CSV " + outputfile + " Finished")

