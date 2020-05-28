#question_05 =
"""
3-6-9
Given an integer n, return a list with each number from 1 to n, 
except if it’s a multiple of 3 or has a 3, 6, or 9 in the number, 
it should be the string “clap”.

Note: return the number as a string.

Example 1:

Input:
n = 16

Output:
[“1”, “2”, “clap”, “4”, “5”, “clap”, “7”, “8”, “clap”, “10”, “11”, “clap”, “clap”, “14”, “clap”, “clap”]

Explanation:
- 3, 6, 9, 12, and 15 are replaced by “clap” since they are divisible by 3.
- 13 is replaced since it has a 3 in the number.
- 16 is replaced since it has a 6 in the number.

Write your code here
"""

number = input()
a = []

for i in range(1,int(number)+1):
    if(i%10!=0):
        if(i%3==0 or (i%10)%3==0):
            a.append("clap")
        else:
            ch = str(i)
            a.append(ch)
    else:
            ch = str(i)
            a.append(ch)

print(a)