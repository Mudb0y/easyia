# Inport dependencies.
import os
from internetarchive import download
from internetarchive import search_items

print ("Welcome to The Internet Archive indexing and downloading tool. \n Please select an option: \n 1. Download item using The Internet Archive item identifier. \n 2. Use The Internet Archive search engine to search for items. \n prompt: ")
option = (input())

if option == "1":
    print ("Please enter the item identifier: ")
    ia_id = input()
    download(ia_id, verbose=True)

elif option == "2":
    print ("Please enter your search term: ")
    search_id = input()
    for i in search_items('identifier:' +search_id):
        print (i)

else:
        print("Please enter a valid option.")
