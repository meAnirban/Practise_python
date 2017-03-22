'''
Created on Mar 4, 2017

@author: ANIRBAN
'''

Objective 
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin: 
The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .

Constraints

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O




class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self,firstName, lastName, idNum, scores):
        self.scr=scores
        Person.__init__(self,firstName, lastName, idNum)
        
    def calculate(self):
        sum2=sum(self.scr)/len(self.scr)
        if(sum2<=100 and sum2>=90):
            grade = 'O'
        elif(sum2<90 and sum2>=80):
            grade= 'E'
        elif(sum2>=70 and sum2<80):
            grade= 'A'
        elif(sum2>=55 and sum2<70):
            grade= 'P'
        elif(sum2>=40 and sum2<55):
            grade= 'D'
        elif(sum2<40):
            grade= 'T'
        return grade
    

    
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())