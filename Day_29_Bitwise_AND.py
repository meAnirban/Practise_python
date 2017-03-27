# 
# 
# 
# Objective 
# Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!
# 
# Task 
# Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.
# 
# Input Format
# 
# The first line contains an integer, , the number of test cases. 
# Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.
# 
# Constraints
# 
# Output Format
# 
# For each test case, print the maximum possible value of  on a new line.
# 
# Sample Input
# 
# 3
# 5 2
# 8 5
# 2 2
# Sample Output
# 
# 1
# 4
# 0
# Explanation
# 
#  
# 
# All possible values of  and  are:
# 
# The maximum possible value of  that is also  is , so we print  on a new line.


import sys


def bitops(n,k):
    max=0
    for i in range(n):
        for j in range(i+1,n+1):
            if(i<j and i&j<k and i&j>max):
                max=i&j
    return max
    
temp=[]
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    if(2<=n and 2<=k):
        temp.append(bitops(n,k))
for x in temp:
    print(x)