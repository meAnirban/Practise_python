# 
# 
# Objective 
# Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!
# 
# Task 
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
# 
# If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Input Format
# 
# The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned. 
# The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).
# 
# Constraints
# 
# Output Format
# 
# Print a single integer denoting the library fine for the book received as input.
# 
# Sample Input
# 
# 9 6 2015
# 6 6 2015
# Sample Output
# 
# 45
# Explanation
# 
# Given the following return dates: 
# Actual:  
# Expected: 
# 
# Because , we know it is less than a year late. 
# Because , we know it's less than a month late. 
# Because , we know that it was returned late (but still within the same month and year).
# 
# Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.




def fine(d0,m0,y0,d1,m1,y1):
    if(y0==y1):
        if(m0==m1):
            if(d0>d1):
                return 15*(d0-d1)
            else:
                return 0
        elif(m0>m1):
            return 500*(m0-m1)
        else:
            return 0
    elif(y0>y1):
        return 10000
    return 0
        


d0,m0,y0=input().strip().split(' ')
d0,m0,y0=[int(d0),int(m0),int(y0)]
d1,m1,y1=input().strip().split(' ')
d1,m1,y1=[int(d1),int(m1),int(y1)]

if(1<=d0<=31 and 1<=m0<=12 and 1<=d1<=31 and 1<=m1<=12):
    print(fine(d0,m0,y0,d1,m1,y1))