#--------------------------------------------------------------------------- 

# file : Exponent Function

# Author : Mazen Sakr 

#-------------------------------------------------------------

#function defintions
def raiseToPower (Number, Exponent) :
    Result= 1
    for counter in range(Exponent) :
        Result = Result*Number
    return Result


#main code : 
print("This program  calculates powers\n")
number = float(input("Please input the number : "))
exponent = int(input("Please input the exponent : "))
print("The result is : " + str(raiseToPower(number,exponent)))