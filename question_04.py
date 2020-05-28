#question_04 =
"""
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.

Write your code bellow
"""

def test_prime(n):
    if (n==1):
        return 0
    elif (n==2):
        return 1
    else:
        for x in range(2,n):
            if(n % x==0):
                return 0
        return 1   


a= input()
s = str(a)
print(type(s))
print(s)
length = len(s)
count=0
for i in range(0,length):
    s= s[-1] + s[:-1]
    a = int(s)
    if(test_prime(a)==1):
        count = count+1
    else:
        continue

print(count)

if(count==length):
    print("TRUE")
else:
    print("FALSE")


