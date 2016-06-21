def mainActivity():
    print "=========================DUDLEY PADLOCK CRACK TOOL===========================\n\n"
    
    THIRD_NUMBER = int(input("Please enter the last number of your padlock: "))
    if THIRD_NUMBER >=40:
        print "Sorry, the number you enter is invalid. Please try again.\n\n"
        mainActivity()

    REMAINDER = THIRD_NUMBER % 4
    FIRST_NUMBER = REMAINDER
    SECOND_NUMBER = FIRST_NUMBER

    if REMAINDER < 2:
        SECOND_NUMBER = SECOND_NUMBER + 2

    else:
        SECOND_NUMBER = SECOND_NUMBER - 2

    print "\nPossible first numbers: \n" ,FIRST_NUMBER

    while FIRST_NUMBER <= 35:
        FIRST_NUMBER = FIRST_NUMBER + 4
        print FIRST_NUMBER

    print "\n\nPossible second numbers: \n" ,SECOND_NUMBER

    while SECOND_NUMBER <= 35:
        SECOND_NUMBER = SECOND_NUMBER + 4
        print SECOND_NUMBER

    print "\n\nAnd your THIRD number is: ",THIRD_NUMBER,"\n\nIf a 2nd # is +/- 2 from the 3rd #, just get rid of it.\n\nProgram has completed.===================================================\n\n\n\nPowered by Python + EugeneOnTheEdge"

mainActivity()
