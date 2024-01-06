#!/usr/bin/env python3

#scriptCalifornia.py

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def readFromFile(inputFileName):

	df = pd.read_csv(inputFileName)

	df = df.drop(columns = ['Data_Revision_Date'])

	df = df.sort_values(['Year','Rank'],ascending = [0,1])

	df = df[['Rank','Name','Count','Sex','Year']]

	df2 = df.loc[df['Sex'] == 'Male']
	df = df.loc[df['Sex'] == 'Female']

    #Saves the sorted files to a specific directory
	folder_path = '/home/undergrad/1/ajanisze/cis2250/TeamProject/sortedFiles/'
	file_name1 = 'sortedFemaleCali.csv'
	file_name2 = 'sortedMaleCali.csv'

	file_path1 = folder_path + file_name1
	file_path2 = folder_path + file_name2

	df.to_csv(file_path1,index = False)
	df2.to_csv(file_path2,index = False)




    #outputFileName = "caliSorted.csv"
    #rank     = []
    #names    = []
    #count    = []
    #gender   = []
    #years    = []
    #total    = 0
    

    #with open (inputFileName) as csvDataFile:
    #    csvReader = csv.reader(csvDataFile, delimiter=',')
    #    for row in csvReader:
    #        years.append(int(row[0]))
    #        tempGender = row[1].strip()
    #        gender.append(tempGender)
    #        rank.append(int(row[2]))
    #        tempName = row[3].strip()
    #        names.append(tempName)
    #        count.append(int(row[4]))
    #        total = total+1

    #print(names)
    #print(count)
    #print(rank)
    #print(gender)
    #print(years)

    #f = open (outputFileName, "w")
    #csvWrite = csv.writer(f, delimiter=",")
    #for i in range(total):
    #   csvWrite.writerow([str(rank[i]), names[i], str(count[i]), gender[i], str(years[i])])
