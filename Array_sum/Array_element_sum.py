'''
Created on Mar 4, 2017

@author: ANIRBAN
'''
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sum=0
for i in range(0,n):
    sum +=arr[i]
    
print(sum)