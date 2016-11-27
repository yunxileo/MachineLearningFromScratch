# -*- coding: UTF-8 -*-
from csv import reader
# Load a CSV file
def load_csv(filename):
    dataset=[]
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        linearr=line.strip().split('\t')
        dataset.append([float(linearr[0]),float(linearr[1])])
    return dataset

# # Convert string column to float
# def str_column_to_float(dataset, column):
# 	for row in dataset:
# 		row[column] = float(row[column].strip().split('\t'))

# Load pima-indians-diabetes dataset
filename = 'F:/python/MachineLearningFromScratch/regression/insurance.csv'
dataset = load_csv(filename)
print(dataset[0])
print(len(dataset[0]))

