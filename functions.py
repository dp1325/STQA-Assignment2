import math

#Main Menu Function
def mainMenu():
    print("Select Option (a, b, or c):")
    print("a) Body Mass Index")
    print("b) Retirement")
    print("c) Exit")
    selection = input("Selection: ")
    print("\n")
    return selection

#Boundary Check Function
def check(input, low, high):
    if(input.isnumeric()==True):
        if(float(input)>=float(low) and float(input)<=float(high)):
            return True
        else:
            return False
    else:
        return False

#BMI Calculation Function
def bmiCalc():

    #input
    feet = input("Height (feet only): ")
    while(check(feet, 0, 10)==False):
        print("Error: Invalid height")
        feet = input("Height (feet only): ")
    inches = input("Height (inches only): ")
    while(check(inches, 0, 11)==False):
        print("Error: Invalid height")
        inches = input("Height (inches only): ")
    weight = input("Weight: ")
    while(check(weight, 0, 1000)==False):
        print("Error: Invalid weight")
        weight = input("Weight: ")

    #calculation
    kg = float(weight) * 0.45
    total = (float(feet) * 12) + float(inches)
    m = float(total) * 0.025
    m2 = m * m
    bmi = round((kg / m2), 1)
    answer = str(bmi)

    #output
    print("\nBMI:", answer)
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<25.0):
        print("Normal weight")
    elif(bmi>=25.0 and bmi<30.0):
        print("Overweight")
    elif(bmi>=30.0):
        print("Obese")

    print("\n")

#Retirement Age Calculation Function
def retCalc():

    #input
    currAge = input("Current Age: ")
    while(check(currAge, 0, 100)==False):
        print("Error: Invalid age")
        currAge = input("Current Age: ")
    salary = input("Annual Salary: ")
    while(check(salary, 0, 100000000)==False):
        print("Error: Invalid salary")
        salary = input("Salary: ")
    saved = input("Percentage Saved: ")
    while(float(saved)<0 or float(saved)>1):
        print("Error: Invalid percentage")
        saved = input("Percentage Saved: ")
    desired = input("Desired Retirement Savings Goal: ")
    while(check(desired, 0, 100000000)==False):
        print("Error: Invalid goal")
        desired = input("Desired Retirement Savings Goal: ")

    #calculation
    spy = (float(salary) * float(saved)) * 1.35
    years = math.ceil(float(desired) / float(spy))
    age = years + float(currAge)

    #output
    if(age<100):
        print("Your goal will be met at age", int(age))
    else:
        print("Your goal will not be met, age:", int(age))

    print("\n")
