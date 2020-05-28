#question_03 =
"""
An anagram I am

Given two strings s0 and s1, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, “listen” and “silent” are anagrams.

Constraints:
- Length of s0 and s1 is at most 5000.

Example 1:

Input:
s0 = “listen”
s1 = “silent”

Output:
True

Example 2:

Input:
s0 = “bedroom”
s1 = “bathroom”

Output:
False

Write your code here
"""
# my own code with new functions
def isanagram(x,s1):
    if(s1.find(x)==-1):
        return 0
    else:
        return 1


def anagram(s0,s1):
    length = len(s0)
    count=0
    for x in s0:
        if(isanagram(x,s1)==1):
            count = count+1
    
    if(count==length):
        print('TRUE')
    else:
        print('FALSE')




s0 = input()
s1 = input()

anagram(s0,s1)


#using counter
from collections import Counter 
  
def anagram1(input1, input2): 
    return Counter(input1) == Counter(input2)  
 
input1 = 'abcd'
input2 = 'dcab'
print(anagram1(input1, input2))