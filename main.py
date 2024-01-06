#!/usr/bin/env python3

#run command: ./main.py -a aus.csv -b cali.csv

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

# Reading files and functions 
from scriptCalifornia import readFromFile
from scriptAustralia import readFromFile2
from function4 import californiaFun4, australiaFun4

def main ( argv ):

    print(argv)
    if argv != ['-a', 'aus.csv', '-b', 'cali.csv']:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"a:b:",["input="] )
    except getopt.GetoptError:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./main.py -a <input file name> -b <input file name>" )
            sys.exit()
        elif opt in ( "-a", "--input1"):
            inputFileName1 = arg #passed into function
        elif opt in ( "-b", "--input2"):
            inputFileName2 = arg #passed into function
            
    #df = pd.read_csv(inputFileName1)

    #print(df)
    readFromFile2(inputFileName1) #function call read from aus.csv 
    readFromFile(inputFileName2) #function call read from cali.csv 

    californiaFun4()
    australiaFun4()

#this needs to be here
if __name__ == "__main__":
    main ( sys.argv[1:] )
    