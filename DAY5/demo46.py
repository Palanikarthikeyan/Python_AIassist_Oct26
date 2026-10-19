'''
Write a python program
filter list of pdf files from login directory 
# To get list of all the files -> os.listdir("C:\\Users\\USERNAME") ->list
# search a pattern line ends with pdf =>re.search("pdf$",<input_str>)
'''
import os
import re
files = os.listdir("C:\\Users\\karth\\")
for var in files:
    if re.search("pdf$",var):
        print(var)