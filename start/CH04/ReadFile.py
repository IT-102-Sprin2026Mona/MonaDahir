#!/usr/bin/env python3
# Sample script that reads from a file
# By  Mona

'''This is to read the file i createed from the script writefile.py'''

#Create a loop to open file and read its contents
with open("hackme.txt", "r") as file:
    contents = file.read()
print("here is someone to hack - info dump")
print(contents)