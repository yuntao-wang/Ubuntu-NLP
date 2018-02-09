# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import relevant packages
import csv
import os
from collections import Counter

import re
import string

from nltk.corpus import stopwords

# remove punctuation
def standard_words(word):
    remove = string.punctuation
    remove = remove.replace("-", "")
    pattern = r"[{}]".format(remove)
    return re.sub(pattern, "", word)

# get word frequency
words=set()
word_freq ={}

for fn in os.listdir('4'):
    with open('4/%s'%fn, newline='', encoding='utf8') as afile:
        lines = csv.reader(afile, delimiter='\t')
        for line in lines:
            for word in standard_words(line[3]).split():
                if word not in stopwords.words("english"):
                    words.add(word.lower())
                    if not word_freq.get(word):
                        word_freq[word] = 1
                    else:
                        word_freq[word] += 1

# tags contain top tags about Ubuntu in StackOverflow
tags =[]
with open("tags.txt", newline='') as all_tags:
    temp = csv.reader(all_tags, delimiter=',')
    for tag in temp:
        tags += tag

d = Counter(word_freq)

ord = d.most_common()

# cross check with Ubuntu tags to select relevant topics
count =0
res =[]
for ele in ord:
    while count<10:
        if ele[0] in tags:
            res.append((ele[0],ele[1]))
            count+=1
        break
print(res)