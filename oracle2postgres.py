#!/usr/bin/python
# oracle to postgres datatype conversion

import numpy
import sys

def cli_args(sys_argv):
    if len(sys_argv) < 1:
        return 0
    else:
        print(sys_argv[0])

def read_mapping():
    # read mapping file
    print("mapping")
    
def read_source():
    # read oracle source file
    print("source")
    with open("create_table_example.txt") as f:
        l = f.read()
        print(l)
    
###### MAIN 
if __name__ == "__main__" :
    print ("Main part")
    if cli_args(sys.argv) == 0:
        print ("Error")
    else:
        read_source()
