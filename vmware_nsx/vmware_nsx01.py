#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   NSX - List all the Compute Managers part of the NSX-T

   Adapted from:
   https://developer.vmware.com/samples/7641/nsxt-get-compute-manager"""

import argparse
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument("--nsxtIP", help="Provide the NSXT IP/FQDN", required=True)
parser.add_argument("--nsxtUser", help="Provide the NSXT Username", required=True)
parser.add_argument("--nsxtPassword", help="Provide the NSXT Password ", required=True)


args = parser.parse_args()

COMPUTE_MANAGER_URL = 'https://'+ args.nsxtIP +'/api/v1/fabric/compute-managers'
TRANSPORT_ZONE_URL = 'https://'+ args.nsxtIP +'/api/v1/transport-zones/'

#This function will get the existing Compute Manager details from NSX-T
def getComputeManager():
    print("Get the details of Existing Compute Managers in the NSX-T")
    print("Running the following URL :" +COMPUTE_MANAGER_URL)
    r= requests.get(COMPUTE_MANAGER_URL, auth=(args.nsxtUser, args.nsxtPassword), verify=False)
    if r.status_code == 200:
        print(r.text)
        print("Able to Get the Existing Compute Managers")
    else:
        print("Looks like NSX is UP and running, Could not get the Existing Compute Manager details")
        print(r.status_code)
        raise Exception(r.text)

def main():
    exit_code = 0
    try:
        getComputeManager()
    except Exception as e:
        print(e)
        exit_code = 1
    finally:
        sys.exit(exit_code)

if __name__ == "__main__":
        main()

