import csv, os
from ftplib import FTP
import pandas as pd
import globus_connect, globus_sdk

#### USAGE HERE ####
host ="cdiac.ornl.gov"
user = ""
password = ""

print("Connecting to {}".format(host))
ftp = FTP(host) ### connect to FTP

#ftp.login() ### UNCOMMENT TO DO STRAIGHT FROM FTP SOURCE.
#print("Logged in :)")

### Note: these are just the UUIDs of the endpoints.
LOCAL_ID = "21a48f1a-f931-11e6-ba95-22000b9a448b"
PETREL_ID = "45a53408-c797-11e6-9c33-22000a1e3b52"

### STEP 1: Connect to the .txt file containing all applicable file information.



### Step 2: Initiate Globus-Transfer from Petrel
def transfer_activate():
    tc = globus_connect.get_globus_client()

    tc.endpoint_autoactivate(PETREL_ID)
    print("PETREL ready for transfer instruction.")
    tc.endpoint_autoactivate(LOCAL_ID)
    print("LOCAL ready for transfer instruction.")

    return tc




def download_file(tc, endpoint_id, globus_path, file_name, local_path):
    # print("downloading file {}".format(globus_path + file_name))
    tdata = globus_sdk.TransferData(tc, endpoint_id, LOCAL_ID)
    tdata.add_item(globus_path + file_name, local_path + file_name)

    result = tc.submit_transfer(tdata)

    while not tc.task_wait(result["task_id"], polling_interval=1, timeout=60):
        pass
        # print("waiting for download: {}".format(globus_path + file_name))

tc = transfer_activate()

# Now put this into a loop. "TOUCH AND DELETE".
#download_file(tc,PETREL_ID, "/cdiac/cdiac.ornl.gov/pub8/oceans/AMT_data/", "AMT1.txt", "/home/tskluzac/")



def delete_file(tc, local_path, file_name):
    print("deleting file {}".format(local_path + file_name))
    ddata = globus_sdk.DeleteData(tc, LOCAL_ID)

    ddata.add_item(local_path + file_name)

    # # Run in case the endpoint deactivated.
    # tc.endpoint_autoactivate(endpoint_id)

    result = tc.submit_delete(ddata)

#delete_file(tc, "/home/tskluzac/", "AMT1.txt")