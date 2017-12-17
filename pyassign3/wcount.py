#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "LiXianghao"
__pkuid__  = "1700011711"
__email__  = "1700011711@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    
    import string
    for c in string.punctuation:
        lines = lines.replace(c,'')

    for number in range(0,10):
        lines = lines.replace(str(number),'')
    
    lines = lines.lower()
    
    list1 = lines.split()
    set1 = set(list1)
    list2 = list(set1)
    fk = {}

    for word1 in list2:
        num = 0
        for word2 in list1:
            if word1 == word2:
                num +=1
        fk[word1] = num
    
    list3 = list(fk.values())
    list3.sort(reverse=True)
    list4 = list3[0:topn]
    sht = {}
    for i in list4:
        for j in list(fk.keys()):
            if fk[j] == i:
                sht[j] = i
    keys = list(sht.keys())
    damn = {}
    for k in keys[0:topn]:
        damn[k] = sht[k]

    for key in damn:
        print(key,'\t',damn[key])

    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
