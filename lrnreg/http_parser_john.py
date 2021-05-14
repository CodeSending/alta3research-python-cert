#!/usr/bin/env python3
import urllib.request
import re
print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()
words = searchFor.split()
for word in words:
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")
    #if re.search(searchFor, searchMe):
    matches = re.findall(word, searchMe)
    #if matches:
    print(f"{word}: found a {len(matches)} matches!")
    #else:
    #    print(f"{word}: no match!")
