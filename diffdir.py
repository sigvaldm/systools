#!/usr/bin/env python

# Lists the differences between two folders
# Usage: ./diffdir.py folder/A folder/B

import os
import sys
import filecmp

root_a = sys.argv[1]
root_b = sys.argv[2]

exists_only_in_a = 0
exists_only_in_b = 0
newest_in_a = 0
newest_in_b = 0
total = 0

def cmp_dirs(dir_a, dir_b):

    global root_a, root_b, exists_only_in_a, exists_only_in_b
    global newest_in_a, newest_in_b, total

    contents_a = os.listdir(dir_a)
    contents_b = os.listdir(dir_b)

    for i in contents_a:
        url_a = os.path.join(dir_a, i)
        url_b = os.path.join(dir_b, i)

        if i in contents_b:
            if os.path.isdir(url_a) and os.path.isdir(url_b):
                cmp_dirs(url_a,url_b)
            elif not filecmp.cmp(url_a, url_b):
                mod_a = os.path.getmtime(url_a)
                mod_b = os.path.getmtime(url_b)
                if mod_a > mod_b:
                    url_recent = url_a
                    newest_in_a += 1
                else:
                    url_recent = url_b
                    newest_in_b += 1
                print("File differs: %s"%(url_recent))
        else:
            print("Exists only in %s: %s"%(root_a,url_a))
            exists_only_in_a += 1

        contents_b.remove(i)
        total = total + 1

    for i in contents_b:
        url_b = os.path.join(dir_b, i)
        print("Exists only in %s: %s"%(root_b,url_b))

        exists_only_in_b +=1
        total += 1

print("Compares file-by-file. When file differs the one last modified is displayed here.")
cmp_dirs(root_a,root_b)
print("\nSUMMARY")
print("%6d entities exists only in %s"%(exists_only_in_a, root_a))
print("%6d entities exists only in %s"%(exists_only_in_b, root_b))
print("%6d entities differs and is last modified in %s"%(newest_in_a, root_a))
print("%6d entities differs and is last modified in %s"%(newest_in_b, root_b))
print("%6d entities are equal"%(total-exists_only_in_a-exists_only_in_b-newest_in_a-newest_in_b))
print("%6d entities in total"%total)
