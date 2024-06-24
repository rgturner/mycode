#!/usr/bin/env python3
# Check user input matches desired value
hostname = input("What value should we set for hostname?")

## User lowercase method to check if criteria is met
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches the config")

## Notify the use that the script has ended
print("Exiting the script")    
