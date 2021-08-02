#imports
import time, sys, random, pickle, os
from replit import db
from art import *
#functions
st = 0.04
def exit_command():
  print("Exit Command!")
  time.sleep(1)
  os.system("clear")
  
  if 1 == 1:
    fn_input()
    operation_input()                                  
    sn_input()
    calculation()
    while 1 == 1:
      newn_input()
      operation_input1()
      calculation2()
def str_error():
    os.system("clear")
    sp("Error! Enter a symbol, not a number!")
    time.sleep(0.5)
    os.system("clear")


def number_error():
    os.system("clear")
    sp("Error! Enter a number only!")
    time.sleep(0.5)
    os.system("clear")


def instructions():
    sp("There are commands in this version of the calculator. for example: x:starts the program again"
       )
    sp("There is xx which closes thr program so you should run it again")


def fn_input():
      while 1 == 1:
          sp("Enter the first number")
          global fn
          fn = input()
          if fn == "x":
            exit_command()
          try:
              fn = float(fn)
              break
          except:
              number_error()


def operation_input():
    while 2 == 2:
        os.system("clear")
        sp(str(fn) + " ___ " + " ___ " + " = " + " ___ ")
        sp("Enter the operation ('+'/'-'/'*'/'/')")
        global operation
        operation = input()
        if operation == "x":
            exit_command()    
        try:
          operation = str(operation)
          break
        except:
          str_error()  


def sn_input():
    while 1 == 1:
        os.system("clear")
        sp(str(fn)+ operation + " ( ___ ) "+" = " + " ___ ")
        global sn
        sn = input()
        if sn == "x":
            exit_command() 
        elif sn == 0 and operation == "/":
          print("Error divder cant be zero")       
        try:
            sn = float(sn)
            break
        except:
            number_error()


def calculation():
    if operation == "+":
        os.system("clear")
        global answer
        answer = float(fn) + float(sn)
        sp(str(fn) + " + " + str(sn) + " = " + str(answer))
    elif operation == "-":
        os.system("clear")
        #global answer
        answer = float(fn) - float(sn)
        sp(str(fn) + " - " + str(sn) + " = " + str(answer))
    elif operation == "*":
        os.system("clear")
        #global answer
        answer = float(fn) * float(sn)
        sp(str(fn) + " * " + str(sn) + " = " + str(answer))
    elif operation == "/":
        os.system("clear")
        #global answer
        answer = float(fn) / float(sn)
        sp(str(fn) + " / " + str(sn) + " = " + str(answer))


def newn_input():
    while 1 == 1:
        time.sleep(1)
        os.system("clear")
        sp(str(answer) + " ___ " + " ( ___ ) " + " = " + " ___ ")
        sp("Enter The new number")
        global newn
        newn = input()
        if newn == "x":
            exit_command()    
        try:
            newn = int(newn)
            break
        except:
            number_error()


def operation_input1():
    while 2 == 2:
        os.system("clear")
        sp(str(answer) + " ( ___ ) " + str(newn) + " = " + " ___ ")
        sp("Enter the operation ('+'/'-'/'*'/'/')")
        global operation
        operation = input()
        if operation == "x":
            exit_command()   
        try:
            operation = str(operation)
            break
        except:
            str_error()


def calculation2():
    if operation == "+":
        os.system("clear")
        global answer
        answer1 = float(answer) + float(newn)
        sp(str(answer) + " + " + str(newn) + " = " + str(answer1))
        answer = answer1
    elif operation == "-":
        os.system("clear")
        #global answer
        answer1 = float(answer) - float(newn)
        sp(str(answer) + " - " + str(newn) + " = " + str(answer1))
        answer = answer1
    elif operation == "*":
        os.system("clear")
        #global answer
        answer1 = float(answer) * float(newn)
        sp(str(answer) + " * " + str(newn) + " = " + str(answer1))
        answer = answer1
    elif operation == "/":
        os.system("clear")
        #global answer
        answer1 = float(answer) / float(newn)
        sp(str(answer) + " / " + str(newn) + " = " + str(answer1))
        answer = answer1

def sp(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)
    print()


#starts
sp("Welcome to the Calculator!")
fn_input()
operation_input()
sn_input()
calculation()
while 1 == 1:
    newn_input()
    operation_input1()
    calculation2()
#ends
