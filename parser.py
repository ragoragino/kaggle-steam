import csv
import argparse
import sys
import tensorflow as tf

# testReader = csv.reader(open("data/steam-200k.csv", newline =''), delimiter=' ', quotechar='|')
testReader = csv.DictReader(
    open('data/steam-200k.csv'), fieldnames=['id', 'name', 'type', 'time'])
count = 0
outputData = {}
for row in testReader:
    if row['id'] not in outputData:
        outputData[row['id']] = [[0, 0, 0],[0]]
    if(row['name'] == "Team Fortress 2" and row['type'] == "purchase"):
        outputData[row['id']][0][0] = 1
    if(row['name'] == "Counter-Strike Global Offensive" and row['type'] == "purchase"):
        outputData[row['id']][0][1] = 1
    if(row['name'] == "Left 4 Dead 2" and row['type'] == "purchase"):
        outputData[row['id']][0][2] = 1
    if(row['name'] == "Dota 2" and row['type'] == "purchase"):
        outputData[row['id']][1][0] = 1


    count += 1

print(outputData)
print("Total number is: " + str(count))
