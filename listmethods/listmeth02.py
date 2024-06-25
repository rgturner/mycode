#!/usr/bin/env python3

''' 
Author: Robert Turner
    Working with Methods
    Run various methods and print their results
'''

def main():
    ''' This is the main program'''
    proto = ["ssh", "http", "https"] # create a list
    protoa = ["ssh", "http", "https"] # create a second list
    print(proto)
    proto.append("dns") # this line will add "dns" to the end of our list
    protoa.append("dns") # this line will add "dns" to the end of our list
    print(proto)
    proto2 = [ 22, 80, 443, 53 ] # a list of common ports
    proto.extend(proto2) # pass proto2 as an argument to the extend method
    print(proto)
    protoa.append(proto2) # pass proto2 as an argument to the append method
    print(protoa)
    proto3 = proto.insert(1,"tcpip") # inserting a value into the list
    print(proto3)
main()
