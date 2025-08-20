# define the tools that math agent can use

from agents import function_tool

@function_tool
def Addition(n1 , n2):
    print(">>>>>> Addition function called >>>>>>>>")
    return f" Addition of {n1} and {n2} is: {n1 + n2}"

@function_tool
def Subtractions(n1,n2):
    print(">>>>>> Subtractions function called >>>>>>>>")
    return f" Subtraction of {n1} and {n2} is: {n1 - n2}"

@function_tool
def Multiplications(n1,n2):
    print(">>>>>> Multiplications function called >>>>>>>>")
    return f" Multiplication of {n1} and {n2} is: {n1 * n2}"

@function_tool
def Divisions(n1,n2):
    print(">>>>>> Divisions function called >>>>>>>>")
    return f" Division of {n1} and {n2} is: {n1 / n2}" if n2 != 0 else " Division by zero error"
