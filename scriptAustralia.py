#!/usr/bin/env python3

#scriptAustralia.py

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def readFromFile2 (inputFileName1):
	df = pd.read_csv(inputFileName1)

	df = df.sort_values(['Year','Rank'],ascending = [0,1])

	df = df[['Rank','Name','Count','Gender','Year']]

	df2 = df.loc[df['Gender'] == 'Male']
	df = df.loc[df['Gender'] == 'Female']

    #Saves the sorted files to a specific directory
	folder_path = '/home/undergrad/1/ajanisze/cis2250/TeamProject/sortedFiles/'

    #Names the files to be saved
	file_name1 = 'sortedFemaleAus.csv'
	file_name2 ='sortedMaleAus.csv'
    
    #Designates the file path and adds the file name
	file_path1 = folder_path + file_name1
	file_path2 = folder_path + file_name2

    #Creates the new CSV files at specified folder path
	df.to_csv(file_path1,index = False)
	df2.to_csv(file_path2,index = False)
