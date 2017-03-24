'''
Created on Mar 4, 2017

@author: ANIRBAN
'''

# Objective 
# Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!
# 
# Consider the following version of Bubble Sort:
# 
# for (int i = 0; i < n; i++) {
#     // Track number of elements swapped during a single array traversal
#     int numberOfSwaps = 0;
#     
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#             numberOfSwaps++;
#         }
#     }
#     
#     // If no elements were swapped during a traversal, array is sorted
#     if (numberOfSwaps == 0) {
#         break;
#     }
# }
# Task 
# Given an array, , of size  containing distinct elements , sort array  in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:
# 
#  
# where  is the number of swaps that took place.
#  
# where  is the first element in the sorted array.
#  
# where  is the last element in the sorted array.
# Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.
# 
# Input Format
# 
# The first line contains an integer, , denoting the number of elements in array . 
# The second line contains  space-separated integers describing , where the  integer is , .
# 
# Constraints
# 
# , 
# Output Format
# 
# There should be  lines of output:
# 
#  
# where  is the number of swaps that took place.
#  
# where  is the first element in the sorted array.
#  
# where  is the last element in the sorted array.
# Sample Input 0
# 
# 3
# 1 2 3
# Sample Output 0
# 
# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
# Sample Input 1
# 
# 3
# 3 2 1
# Sample Output 1
# 
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
# Explanation
# 
# Sample Case 1: 
# The array is already sorted, so  swaps take place and we print the necessary  lines of output shown above.
# 
# Sample Case 2: 
# The array is not sorted, and its initial values are: . The following  swaps take place:
# 
# At this point the array is sorted and we print the necessary  lines of output shown above.



import sys

class sorting:
    def swap(self,a,n):
        self.a=a
        self.n=n
        self.num_swap=0
        for i in range(0,n):
            for j in range(0,n-1):
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
                    self.num_swap+=1
            if(self.num_swap==0):
                break
           
    def display(self,a):
        print("Array is sorted in "+str(self.num_swap)+" swaps.")
        print("First Element: "+str(self.a[0]))
        print("Last Element: "+str(self.a[-1]))
    
        

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
obj = sorting()
obj.display(obj.swap(a,n))