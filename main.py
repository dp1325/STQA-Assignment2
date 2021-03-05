import functions

#Run until user exits
run = 1;
while(run == 1):

    #Main Menu
    selection = functions.mainMenu()

    #BMI
    if(selection == "a"):
        functions.bmiCalc()

    #Retirement
    elif(selection == "b"):
        functions.retCalc()

    #Exit Program
    elif(selection == "c"):
        run = 0
        exit()

    #Invalid Input
    else:
        print("Error: invalid selection, please choose again\n")
