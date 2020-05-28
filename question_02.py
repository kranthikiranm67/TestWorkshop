#question_02 = 
"""
Given a query string s and a list of all possible words,
return all words that have s as a suffix.

Example 1:
Input:
s = “ed”
words = [“called”, “aged”, “land”]

Output:
[“called”, “aged”]

Explanation:
Only called and aged ends with ed.

Example 2:
Input:
s = “d”
words = [“helped”,  “held”, “land”, “mat”, “cat”, “bold”]

Output:
[“helped”,  “held”, “land”, “bold”]

Explanation:
All these words ends with d, except for “mat” and “cat”.

Write your code bellow
"""

def suffix(s,query):
    
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
    if(suffix(s,query)==1):
        continue
    else:
        print('"',end='')
        strg=suffix(s,query)
        if(count<3):
            print(strg,'",',end='')
        else:
            print(strg,'"',end='')

print(']')
