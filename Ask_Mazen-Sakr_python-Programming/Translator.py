#--------------------------------------------------------------------------- 

# file : translator Function

# Author : Mazen Sakr 

#-------------------------------------------------------------

#function defintions
def translate (phrase) :
    translation = ""
    for letter in phrase :
        if letter in "AEIOUaeiou" :
            if letter.isupper() :
                translation = translation + 'B'
            else :
                translation = translation + 'b'
        else : 
            translation = translation + letter 
    return translation


#main code : 
print("This program is a banana language translator\n")
print(translate(input("Please input phrase to be translated : ")))