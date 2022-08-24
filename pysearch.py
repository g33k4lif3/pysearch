#Searches directories for a specific file
#Author: TM
#Created: 8/24/2022

import os
import sys
import time

print('\n' * 80) #clear screen

#print (sys.argv)

if len(sys.argv) == 1:
    print ("No arguments detected")
    print ("Example: Command line usage format: pysearch.py photo.jpg C:\\Users")
    f=input("Enter name of file to look for (e.g. photo.jpg): ")
    d=input("Enter name of directory to search (e.g. C:\\Users): ")
else:
    f=sys.argv[1]
    d=sys.argv[2].replace("\\\\", "\\")

def pysearch(filename, dir):
    start_time = time.time()
    found=False
    for root, dirs, files in os.walk(dir):
        for file in files:
            print ("comparing " + file + " with " + filename + " in " + root)
            if file==filename:
                print ("File found in %s seconds: " % (time.time() - start_time) + root + "\\" + str(file))
                found=True
                break
        if found:
            break
    if not found:
        print ("File: " + filename + " not found in " + dir)

pysearch(f,d)