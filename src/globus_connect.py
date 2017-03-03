from __future__ import print_function
import os, time, csv
import traceback, globus_sdk
from hashlib import sha256
from re import compile

# This is not needed after first login.
CLIENT_ID = 'a4eb161f-7c0f-486e-ad06-28cc3bf01ce8'

### Should move these to System Vars for security.
AUTH_TOKEN = "AQBYuyQ6AAAAAAAEj5ZMjnWX8k8IXuuJUIGqwA-8s1ETu2Y1zf0MB-q7clGlPEv2KfUNMQArEENZepeTM-Vc"
TRANSFER_TOKEN = "AQBYuyQ6AAAAAAAEj5cXufToCARHFXBMQrBSCN3ODpmGssRRYqXsNDKHyHnq1_HjTgUUu-1ZsBrPe-79ePMY"

def get_tokens():

    client = globus_sdk.NativeAppAuthClient(CLIENT_ID)
    client.oauth2_start_flow_native_app()

    authorize_url = client.oauth2_get_authorize_url()
    print('Please go to this URL and login: {0}'.format(authorize_url))

    # this is to work on Python2 and Python3 -- you can just use raw_input() or
    # input() for your specific version
    get_input = getattr(__builtins__, 'raw_input', input)
    auth_code = get_input(
        'Please enter the code you get after login here: ').strip()
    token_response = client.oauth2_exchange_code_for_tokens(auth_code)

    globus_auth_data = token_response.by_resource_server['auth.globus.org']
    globus_transfer_data = token_response.by_resource_server['transfer.api.globus.org']

    # most specifically, you want these tokens as strings
    AUTH_TOKEN = globus_auth_data['access_token']
    TRANSFER_TOKEN = globus_transfer_data['access_token']
    print("Copy this into AUTH_TOKEN Field: " + AUTH_TOKEN)
    print("Copy this into TRANSFER_TOKEN Field: " + TRANSFER_TOKEN)

### Get Globus-Client which checks against the TRANSFER_TOKEN --- Allows us to make transfers
def get_globus_client():
    authorizer = globus_sdk.AccessTokenAuthorizer(TRANSFER_TOKEN)
    tc = globus_sdk.TransferClient(authorizer=authorizer)
    print("Globus Client ACTIVE at address ", tc)
    return tc

# Ensure that your local endpoint is in this list. Otherwise your transfer will fail.
def get_my_endpoints():
    for ep in (get_globus_client()).endpoint_search(filter_scope="my-endpoints"):
        print("[{}] {}".format(ep["id"], ep["display_name"]))

#get_globus_client()
get_my_endpoints()
