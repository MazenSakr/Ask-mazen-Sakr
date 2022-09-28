#--------------------------------------------------------------------------- 

# file : Advanced calculator 

# Author : Mazen Sakr 

#-------------------------------------------------------------


#main code : 

#taking input 

print("This is an advanced calculator\n") 

number1 = float(input("Please input the first number : ")) 

operator = input("Please input operator : ") 

number2 = float(input("Please input the second number : "))


#processing and output 

if operator == '+' : 
 print(number1+number2) 

elif operator == '-' : 
 print(number1-number2) 

elif operator == '/' : 
 print(number1/number2) 

elif operator == '*' : 
 print(number1*number2) 

else : 
 print("Invalid operator")