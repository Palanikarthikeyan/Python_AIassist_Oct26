'''
Write a python program
filter list of pdf /csv files from login directory 
'''
import os
import re
files = os.listdir("C:\\Users\\karth\\")
for var in files:
    if re.search("pdf$|csv$",var):
        print(var)