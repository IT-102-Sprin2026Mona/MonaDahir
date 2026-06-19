#!/usr/bin/env python3
# Script that scans web server logs for 404 errorsA

"""
The purpose of this script is to return 404 source IPs if found. 
"""

# Libraries utilized
import re

def main():

    LOG_FILE = "C:\Users\justincase\Desktop\IT.102\MonaDahir\start\CH07\access.log"

    with open(LOG_FILE, "r") as f:
        for line in f:

            #IP address is the first field
            ip = line.sprlit()[0]

            #Search for status code 404
            match = re.search(r' 404', line)

            if match:
                print(ip)

if __name__ == "__main__":
    main()
