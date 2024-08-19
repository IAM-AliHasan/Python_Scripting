
import sys
def add(num1,num2):
    x=num1+num2
    return x

def mul(num1,num2):
    x=num1*num2
    return x
def divide(num1,num2):
    x=num1/num2
    return x



num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])

if operation == "add":
    x=add(num1,num2)
    print("The sum of two numbers is: ",x)
else :
    Print("Please provide the valid argument")
