from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from decimal import *
from collections import Counter
from collections import OrderedDict
from string import digits
import csv
import re
import string

def split_string(my_list):
#inputs list of comments / splits the text / outputs frequency of all words

    word_list = []

    for comment in my_list:
        comment=comment.lower()
        #remove uppercase

        comment = re.sub(r'[^\w\s]','',comment)
        table = str.maketrans({key: None for key in string.punctuation})
        comment = comment.translate(table)
        #removes punctuation

        word_list += comment.split()
        #splits string into list of words
        
        unique_set=set(word_list)
        unique_count=len(set(word_list))-1
        #total count of unique words

    print(unique_count)                                                                 
    freq = Counter(word_list)
    print(freq)
    return(freq, unique_count)

def get_comments():

    analyzer = SentimentIntensityAnalyzer()
    my_list = [] #list of comments

    with open ('result.csv' , newline='') as f:
        reader = csv.reader(f)
        #reads everything in csv and stores in reader

        for row in reader:
            vs = analyzer.polarity_scores(row[2])
            my_list += [row[2]]

    return my_list

if __name__ == '__main__':
  my_list = get_comments()
  split_string(my_list)                        
