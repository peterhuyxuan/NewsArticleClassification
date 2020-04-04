from collections import OrderedDict
import pandas as pd
import csv
import copy

# This function is run for each unique word
# it calculates the relevant articles to the word over all articles in the topic
# and calculates the average proportion of each article for which the word composes 

def wordinTopic(wordNum,topics,wordlist,frequency,proportion):
    for i in range(len(topics)):
        for row in topics[i]:
            c=row[1].count(wordlist[wordNum])
            if c != 0:
                frequency[i+1][wordNum]+=1
                proportion[i+1][wordNum]+=c/len(row[1])
        if frequency[i+1][wordNum] != 0:
            proportion[i+1][wordNum]/=frequency[i+1][wordNum]
            frequency[i+1][wordNum]/=len(topics[i])

# Reading the csv file into a Dataframe
df=pd.read_csv('training.csv')

# Creating a list of lists from the Dataframe
training=[list(row) for row in df.values]

# Replace the article_words column with a list of each word 
# delimited by a comma, and then add every unique word to a new list
wordlist=[]
for row in training:
    row[1]=row[1].split(',')
    wordlist+=row[1]
    wordlist=list(OrderedDict.fromkeys(wordlist))
# Sort the list in alphabetical order
wordlist=sorted(wordlist)

# Create lists to hold all articles of a respective topic
act,bpp,dfc,dmm,fxm,hlt,mnm,sat,shl,spt = ([] for i in range(10))
# Create a superlist to hold the topic lists
topics=[act,bpp,dfc,dmm,fxm,hlt,mnm,sat,shl,spt]

# Sort all articles into their respective sublists
for row in training:
    if row[2] == 'ARTS CULTURE ENTERTAINMENT':
        act.append(row)
    elif row[2] == 'BIOGRAPHIES PERSONALITIES PEOPLE':
        bpp.append(row)
    elif row[2] == 'DEFENCE':
        dfc.append(row)
    elif row[2] == 'DOMESTIC MARKETS':
        dmm.append(row)
    elif row[2] == 'FOREX MARKETS':
        fxm.append(row)
    elif row[2] == 'HEALTH':
        hlt.append(row)
    elif row[2] == 'MONEY MARKETS':
        mnm.append(row)
    elif row[2] == 'SCIENCE AND TECHNOLOGY':
        sat.append(row)
    elif row[2] == 'SHARE LISTINGS':
        shl.append(row)
    elif row[2] == 'SPORTS':
        spt.append(row)

# Create the parallel lists that will contain the calculated data
# 1st list: Every unique word, 2nd-11th list: Values of the calculations
proportion=[wordlist]
for i in range(10):
    proportion.append([0]*len(wordlist))
frequency=copy.deepcopy(proportion)

# Run the calculations for every unique word in the dataset
for i in range(len(wordlist)):
    wordinTopic(i,topics,wordlist,frequency,proportion)

# Print the resulting tables to csv files
with open('frequency.csv', 'w', newline="") as f:
    w=csv.writer(f)
    w.writerows(list(map(list, zip(*frequency))))
    
with open('proportion.csv', 'w', newline="") as p:
    w=csv.writer(p)
    w.writerows(list(map(list, zip(*proportion))))
    

            
    
    



















