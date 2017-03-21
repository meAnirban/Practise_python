'''
Created on Mar 4, 2017

@author: ANIRBAN
'''
import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

A=0
B=0
if(a0<=100 and a1<=100 and a2<=100 and b0<=100 and b1<=100 and b2 <=100):
    for i in range(0,3):
        if(globals()['a'+str(i)] < globals()['b'+str(i)]):
            B+=1
        elif(globals()['a'+str(i)] > globals()['b'+str(i)]):
            A+=1
        
print(str(A)+" "+str(B))