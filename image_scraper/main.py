import os, shutil
from ftplib import *
import wget

''' This file extracts a file from CDIAC, allows the user to run any type of predefined compute on it, and then ejects
the file from the OS.  This is useful for commodity machines to save space.  '''''

# import NAME_OF_YOUR_MODULE

fail_num = 0
with open('cdiac_images2017.txt', 'rb') as f:

    for line in f:

        try:
            url = "ftp://cdiac.ornl.gov" + line.rstrip()
            filename = wget.download(url)

            ###########################################

        except:
            fail_num +=1
            print("Dead-Paths: " + str(fail_num))

            continue #Break loop iteration.


        ################# DO YOUR COMPUTE #####################



       print(filename)

        #######################################################

        #Bye, Felicia.
        os.remove(filename)









