#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def find_char(char_list):
    names = []  # list to return back of decoded names
    for x in char_list:
        # send HTTP GET to one of the entries within the list
        r = requests.get(x)
        decodedjson = r.json() # decode the JSON on the response
        names.append(decodedjson.get("name"))  # this returns the housename and adds it to our list
    return names  # when operation is over, send it back

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        
        house = []
        print("Belongs to these houses")
        for house in find_char(got_dj.get("allegiances")):
            print(house)
                
        # if no house found  print("Doesn't belong to a house")
        if len(house) == 0:
            print("Doesn't belong to a house")

if __name__ == "__main__":
        main()

