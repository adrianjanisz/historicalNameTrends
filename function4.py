#!/usr/bin/env python3

#scriptAustralia.py

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def californiaFun4 ():

    maleNames = []
    sharedNames = []
    counter = 0
    numOfNames = 0
    temp = 0

    with open ("sortedFiles/sortedMaleCali.csv") as csvData1:
        csvReader1 = csv.reader(csvData1, delimiter = ',')
        for row in csvReader1:
            if counter == 0:
                counter += 1
            else:
                maleNames.append(row[1])

    with open ("sortedFiles/sortedFemaleCali.csv") as csvData2:
        csvReader2 = csv.reader(csvData2, delimiter = ',')
        for row in csvReader2:
            if counter == 0:
                counter += 1
            else:
                temp = maleNames.count(row[1])
                if temp > 1:
                    sharedNames.append(row[1])
                    temp = 0
                    numOfNames += 1

    if numOfNames == 0:
        print("There are no names that appear in both male and female lists of California names.")
    else:
        print("There are " + str(numOfNames) + " names that appear in both male and female lists of California names:")
        for name in sharedNames:
            if counter2 == numOfNames:
                print(name+". ")
            else:
                print(name+", ", end = '')
                counter2 += 1

def australiaFun4():
    
    maleNames = []
    sharedNames = []
    counter = 0
    numOfNames = 0
    temp = 0
    counter2 = 1

    with open ("sortedFiles/sortedMaleAus.csv") as csvData1:
        csvReader1 = csv.reader(csvData1, delimiter = ',')
        for row in csvReader1:
            if counter == 0:
                counter += 1
            else:
                maleNames.append(row[1])

    with open ("sortedFiles/sortedFemaleAus.csv") as csvData2:
        csvReader2 = csv.reader(csvData2, delimiter = ',')
        for row in csvReader2:
            if counter == 0:
                counter += 1
            else:
                temp = maleNames.count(row[1])
                if temp > 1:
                    if row[1] not in sharedNames:
                        sharedNames.append(row[1])
                        numOfNames += 1
                    temp = 0

    if numOfNames == 0:
        print("There are no names that appear in both male and female lists of Australia names.")
    else:
        print("There are " + str(numOfNames) + " names that appear in both male and female lists of Australia names:")
        for name in sharedNames:
            if counter2 == numOfNames:
                print(name+". ")
            else:
                print(name+", ", end = '')
                counter2 += 1