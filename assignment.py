#!python3
# Volume Calculator
# Feel free to rename your variables
import math
from typing import Counter 

def cone(measurements):
    radius=measurements[1]
    height=measurements[2]
    v=(1/3)*height*math.pi*math.pow(radius,2)
    return v

def pyramid(measurements):
    length=measurements[1]
    width=measurements[2]
    height=measurements[3]
    v=(1/3)*length*width*height
    return v

def cube(measurements):
    side=measurements[1]
    v=math.pow[side,3]
    return v

def sphere(measurements):
    radius=measurements[1]
    v=(4/3)*math.pi*math.pow(radius,3)
    return v

def rectangularprism(measurements):
    length=measurements[1]
    width=measurements[2]
    height=measurements[3]
    v=length*width*height
    return v

def cylinder(measurements):
    radius=measurements[1]
    height=measurements[2]
    v=math.pi*height *math.pow(radius,2)

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("================================")
    print("Welcome to use volume calculator")
    print("================================")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("To use this calculator: ")
    print("step1: choose a shape")
    print("step2: enter the parameters for the shape")
    print("step3: the program will give you the answer")
    return None

def getParams():
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    print("choose your object shape ")
    print("1 cone ")
    print("2 pyramid")
    print("3 cube")
    print("4 rectangular prism")
    print("5 sphere")
    print("6 cylinder\n")
    shape=input("enter a shape: ").strip()
    if shape=="cone" or shape=="1":
        x=("enter the radius:")
        y=("enter the height:")
        prompts=[1,x,y]
        return prompts
    elif shape=="praymid" or shape=="2":
        x=("enter the length:")
        y=("enter the width:")
        z=("enter the height:")
        prompts=[2,x,y,z]
        return prompts
    elif shape=="cube" or shape=="3":
        x=("enter the side")
        prompts=[3,x]
        return prompts
    elif shape=="rectangular prism" or shape=="4":
        x=("enter the length:")
        y=("enter the width:")
        z=("enter the height:")
        prompts=[4,x,y,z]
        return prompts
    elif shape=="sphere" or shape=="5":
        x=("enter the radius:")
        prompts=[5,x]
        return prompts
    elif shape=="cylinder" or shape=="6":
        x=("enter the radius:")
        y=("enter the height:")
        prompts=[6,x,y]
        return prompts
    else:
        return[0,"invaid shape"]

def getInputs(prompts):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements=[0]
    if prompts[0]==1:
        measurements[0]=1
        for x in range(2):
            measurements.append(float(input(prompts[x+1])))
    elif prompts[0]==2:
        measurements[0]=2
        for x in range(3):  
            measurements.append(float(input(prompts[x+1])))
    elif prompts[0]==3:
        measurements[0]=3
        measurements.append(float(input(prompts[1])))
    elif prompts[0]==4:
        measurements[0]=4
        for x in range(3):  
            measurements.append(float(input(prompts[x+1])))
    elif prompts[0]==5:
        measurements[0]=5
        measurements.append(float(input(prompts[1])))
    elif prompts[0]==6:
        measurements[0]=6
        for x in range(2):
            measurements.append(float(input(prompts[x+1])))
    elif prompts[0]==0:
        print(prompts[1])
        measurements[0]="sorry"
    return measurements

def calculate(measurements):
    if measurements[0]==1:
        answer=cone(measurements)
        return answer
    elif measurements[0]==2:
        answer=pyramid(measurements)
        return answer
    elif measurements[0]==3:
        answer=cube(measurements)
        return answer
    elif measurements[0]==4:
        answer=rectangularprism(measurements)
        return answer
    elif measurements[0]==5:
        answer=sphere(measurements)
        return answer
    elif measurements[0]==6:
        answer=cylinder(measurements)
        return answer
    elif measurements[0]=="sorry":
        return None

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    while True:
        output=calculate(getInputs(getParams()))
        if output==None:
            pass
        else:
            print("the volume is",round(output,3))
            c=input("do you want to quit?")
            if c=="yes":
                print("goodbye")
                break
            else:
                pass
        

main()
