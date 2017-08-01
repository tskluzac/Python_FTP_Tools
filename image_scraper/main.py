import os, shutil
from ftplib import *
import wget

''' This file extracts a file from CDIAC, allows the user to run any type of predefined compute on it, and then ejects
the file from the OS.  This is useful for commodity machines to save space.  '''''

# import NAME_OF_YOUR_MODULE

success_num = 0
fail_num = 0

with open('cdiac_images2017.txt', 'rb') as f:

    for line in f:

        try:
            url = "ftp://cdiac.ornl.gov" + line.rstrip()
            filename = wget.download(url)
            success_num += 1
            print("...Successful Download Number " + str(success_num))

       	###########################################

        except: #TODO: Make less vague.
            #This whole Except statement is here to account for download failures, network interrupts, and non-ascii chars in the path.  
            fail_num +=1
            print("Dead Path Number " + str(fail_num))

            continue #Break loop iteration.


        ################# DO YOUR COMPUTE #####################
        

       #Call your functions in here.  




        #######################################################

        #Bye, Felicia. (Delete the file)
        os.remove(filename)









