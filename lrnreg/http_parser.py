#!/usr/bin/env python3
import urllib.request
import re
import crayons

url = ""
urls = []

while url != "q":
    url = input('Where should we search? (Type in "q" to end search url input)')
    if url != "q":
        urls.append(url)
print(urls)

searchfor = ""
searchforlist = []

while searchfor != "q":
    searchfor = input("Great! So we'll try to open this url " + str(url) + "to search for the phrase:")
    if searchfor != "q":
        searchforlist.append(searchfor)
print(searchforlist)

searchcounter = 0
searchMe = []

for site in urls:
    searchMe = urllib.request.urlopen(site).read().decode("utf-8")
    for searchterm in searchforlist:
#        searchMe = urllib.request.urlopen(site).read().decode("utf-8")
        if re.search(searchterm, searchMe):
            searchcounter += 1
            print('Found a match on search term "' + (crayons.yellow(searchterm)) + '"  in site "' + (crayons.red(site)) + '"!"')

        else:
            print(crayons.green('No match on term "' + searchterm + '" in site "' + site + '" :('))

print("Total hits are " + (crayons.red(str(searchcounter))) + "!")
