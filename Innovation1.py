#! /usr/bin/env python

from random import randint   
import argparse
import numpy as np
import matplotlib.pyplot as plt

"""
This is the innovation program, I am going to write about a math program
to generate questions for user to take, after an user is completed the test,
the program will generate the result and write to excel sheet,
finallyh draw a graph.

1. first method:take_input is to take the user arguments from command line
   and determin how many addition, subtraction,and multiplication
   generate the questions.
2. 2nd method:generate_question is to compare the answers to correct answer,
   once you have a score,and write the score to  a csv file
3. Final method: draw_graph plot them into a graph in excel and have a total
   picture. 
4. I am adding this one.   

5.What if I have this one.
 
"""

def take_input():
    
    # This method will take 3 command line argument number from user and
    # determine on number of addition, subtraction, and multiplication
    # exercise problem.
    
    parser = argparse.ArgumentParser(description='Generate 10 math problems.')
    parser.add_argument('add_times',
                        type = int,
                        help = "The number of addition question:")
    parser.add_argument('subtraction_times',
                        type = int,
                        default=1,
                        nargs='?',
                        help="(OPTIONAL) The number of subtraction question")
    parser.add_argument('multiplication_times',
                        type = int,
                        default=1,
                        nargs='?',
                        help="OPTIONAL The number of multiplication question")
    args=parser.parse_args()
    add_times = args.add_times
    subtraction_times = args.subtraction_times
    multiplication_times = args.multiplication_times 
    print ("Generate  %d addition, %d subtraction, and %d multiplication"% \
           (add_times,subtraction_times,multiplication_times))
    return(add_times, subtraction_times, multiplication_times)
    

def generate_question(add,sub,mul):
    
    # This method will generate a mixed of addition, subtraction,
    # and multiplication problem, according to a user's input argument.
    # Afterward, it will write the problems into an excel sheet.
    
    iter =1
    ops =''
    dict1 = {'add':add,'sub':sub,'mul':mul}
    
    for key1 in dict1.keys():
        iter =1 
        while iter <= dict1[key1]:
            a=randint(0,99)
            b=randint(0,99)
            if key1 == 'add':
                result = a + b
            elif key1 == 'sub':
                result = a - b
            else:
                result = a * b
            print (a, key1 ,b,'=', result)
            iter+=2
           
    
def draw_graph():
    
    # This method will take data from a result.csv file and plot them into a
    # graph. 
    
    Iteration,Percent =np.genfromtxt ('/Users/peterchao1/Desktop/WorkFile/result.csv',delimiter=',',unpack=True) 
    plt.plot(Iteration, Percent) 
    plt.title('Math Test') 
    plt.xlabel('Iteration') 
    plt.ylabel('Result (Percentage%)')       
    plt.show() 
 
 
def Main():
    # The main method with 
    
    add,sub,mul=take_input()
    generate_question(add ,sub,mul)
    draw_graph()


if __name__ == '__main__':
    Main()
