#question_01 = 
"""
Given a query string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “de”
words = [“dog”, “deal”, “deer”]

Output:
[“deal”, “deer”]

Explanation:
Only deal and deer begin with de.

Example 2:

Input:
s = “b”
words = [“banana”, “binary”, “carrot”, “bit”, “boar”]

Output:
[“banana”, “binary”, “bit”, “boar”]

Explanation:
All these words start with b, except for “carrot”.

Write your code bellow

"""

def prefix(s,query):
    
    if(s.find(query)==-1):
        return 1
    else:
        return s
    

query = input()
wordinput = input()
words = wordinput.split()
print(len(words))
print('[',end=''),
count = 0
for s in words:
    count = count+1
    if(prefix(s,query)==1):
        continue
    else:
        print('"',end='')
        strg=prefix(s,query)
        if(count<3):
            print(strg,'",',end='')
        else:
            print(strg,'"',end='')

print(']')


