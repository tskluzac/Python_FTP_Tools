from ftplib import FTP
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
LOCAL_PATH = "/src/"

### STEP 1: Connect to the .txt file containing all applicable file information.
pet_list = "/src/pub8_list.txt"

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
    down_ins = globus_sdk.TransferData(tc, endpoint_id, LOCAL_ID)
    down_ins.add_item(globus_path + file_name, local_path + file_name)

    result = tc.submit_transfer(down_ins)

    while not tc.task_wait(result["task_id"], polling_interval=1, timeout=20): #Need to speed up the wait-times.
        pass
        # print("waiting for download: {}".format(globus_path + file_name))

tc = transfer_activate()


def delete_file(tc, local_path, file_name):

    print("Deleting: {}".format(local_path + file_name))

    try:
        del_ins = globus_sdk.DeleteData(tc, LOCAL_ID)
        del_ins.add_item(local_path + file_name)

        # # Run in case the endpoint deactivated.
        # tc.endpoint_autoactivate(endpoint_id)

        result = tc.submit_delete(del_ins)
    except:
        pass

#Test files.
#download_file(tc, PETREL_ID, "/cdiac/cdiac.ornl.gov/pub8/oceans/AMT_data/", "AMT1.txt", "/home/tskluzac/")
#delete_file(tc, "/home/tskluzac/", "AMT1.txt")


# Now put this into a loop. "TOUCH AND DELETE".

def petrel_scan(tc, endpoint_id, start_file_number, local_path):
    #Scan all files in .txt file..

    with open(pet_list) as f:
        for line in f:
            full_file_name = line
            globus_path, file_name = full_file_name.strip().rsplit("/", 1)
            globus_path += "/"

            extension = file_name.split('.', 1)[1].strip() if '.' in file_name else "no extension"

            download_file(tc, PETREL_ID, globus_path, file_name, LOCAL_PATH)
            print("File downloaded.")
            #TODO: EXTRACT SCHEMA INSTRUCTION.
            delete_file(tc, LOCAL_PATH, file_name)
            print("File deleted.")

#tc = transfer_activate()

petrel_scan(tc, PETREL_ID, 1, LOCAL_PATH)