#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching
import argparse
import socket



EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name.lower(), pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def parse_args():
    """runtime code"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "lookfor",
            metavar="lookfor",
            nargs="+",
            help='Enter a pattern for file matching',
            type=str,
            )    
    parser.add_argument(
            "--lookwhere",
            dest="lookwhere",
            help='Enter a path for where to search',
            required=True,
            #type=str,
            action="store_true",
            )
    parser.set_defaults(stdout=False, annotate=False)
    return parser.parse_args() 

def main():
    args = parse_args()
    print(args.lookwhere)
#        print("Results: ", find(arg.lookfor,args.lookwhere) # call function

main()

