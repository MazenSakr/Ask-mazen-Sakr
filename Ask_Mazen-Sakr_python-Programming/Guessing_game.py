#--------------------------------------------------------------------------- 

# file : Guessing game 

# Author : Mazen Sakr 

#-------------------------------------------------------------


#main code : 
print("This is a guessing game : \n")
secretWord = "Help!!"
guessCount = 0
guess =  ""
while guess !=secretWord and guessCount < 3 :
    guess = input("Please input your guess : ")
    guessCount = guessCount + 1
if guess != secretWord :
    print("Out of guesses, you lose")
else :
    print ("You Win!!")