# Inport dependencies.
import os, sys
from internetarchive import download, search_items

print ("Welcome to The Internet Archive indexing and downloading tool. \n Please select an option: \n 1. Download item using The Internet Archive item identifier. \n 2. Use The Internet Archive search engine to search for items.")
option = input("prompt: ")

if option.isdigit == False:
    sys.exit("Please enter an integer.")

if option == "1":
    ia_id = input("Please enter the item identifier: ")
    download(ia_id, verbose=True)

elif option == "2":
    search_id = input("Please enter your search term: ")
    for i in search_items('identifier:' +search_id):
        print (i)

else:
    print("Please enter a valid option.")
