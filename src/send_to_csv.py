import os
import glob
import random

randomNum = str(random.randint(0,200000))
outputfile = "/home/tskluzac/PycharmProjects/CDIAC_scraper/cdiac_site"+randomNum



def  writer(filepath_size_array):
    with open(outputfile, 'a') as summary:
        summary.write(str("File Path") + ',' + str("FileSize") + '\n')

        for item in filepath_size_array:
            filename = item[0]
            print(filename)
            filesize = item[1]
            print(filesize)

            with open(outputfile +'.csv', 'a') as summary:
                summary.write(str(filename) + ',' +
                          str(filesize) + '\n')
    print("CSV Finished")

