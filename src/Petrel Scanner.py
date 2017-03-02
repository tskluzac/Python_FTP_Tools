import csv, os
from ftplib import FTP
import pandas as pd

#### USAGE HERE ####
host ="cdiac.ornl.gov"
user = ""
password = ""

print("Connecting to {}".format(host))
ftp = FTP(host) ### connect to FTP
ftp.login()

print("Logged in :)")


### STEP 1: Connect to the csv file
df = pd.DataFrame(pd.read_csv("/home/tskluzac/Downloads/data_pub8.csv")).values.T.tolist()

#s =df.ix[:,0]

### Step 2: Iterate over each row.
i = 0
for item in df[0]:
    #if i> 10: break

    full_path = str('ftp://'+host+item)

    #data = urlopen(full_path).read()
    filename = full_path.split('/')[-1]
    filepath = full_path.split('/')[:-2]


    # for item in filepath:
    #     filepath =

    #ftp.cwd(filename)
    #print

    #print(filename, filepath)



    # try:
    #     print("Request " + i)
    #     req = urllib2.Request(full_path)
    #     print("Response " + i)
    #     response = urllib2.urlopen(req)
    #     print("Page Access " +i)
    #     the_page = response.read()
    # except:
    #     pass

    i+=1
    #urllib.urlretrieve('')
    #print(ftp.cwd(item))


### STEP 2: Iterate through each element

    ### STEP 3: For all zip, tar, z files try extracting them into zip-folder.
    ### STEP 4: If it fails --- pass.

###STEP 5: Push to Globus.