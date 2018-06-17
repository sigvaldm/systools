#!/usr/bin/env python

# Identifies possibly duplicate subdirectories in a directory
# Usage: ./dupdir.py path/to/root/folder

import os
import sys
import hashlib

hashlist = []

def traverse(dir):
    contents = os.listdir(dir)
    roothash = ''
    for fname in contents:
        roothash += fname + ' '
        url = os.path.join(dir,fname)
        if os.path.isdir(url):
            roothash += '( ' + traverse(url) + ') '
    roothash = hashlib.sha1(roothash).hexdigest()
    hashlist.append((dir,roothash))
    return roothash + ' '

traverse(sys.argv[1])
hashlist.sort(lambda a,b: cmp(a[1],b[1]))

prevurl = ''
prevsha = ''
duplicates = dict()
for url, sha in hashlist:
    if(sha==prevsha):
        if not sha in duplicates:
            duplicates[sha] = set()
        duplicates[sha].update([prevurl, url])
    prevurl = url
    prevsha = sha

prefix = ""
print("Each block contains URL with presumably equal folders")
print("NB: Only filenames are checked, contents may differ.")
print("-"*80)
for dup in duplicates.values():
    lst = "\n".join([prefix+str(i) for i in dup])
    print(lst)
    print("-"*80)
