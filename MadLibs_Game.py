#---------------------------------------------------------------------------
# file : Madlibs
# Author : mazen sakr
#-------------------------------------------------------------

#main code :
print("This is a madlibs game, Please input words into the empty spaces\n")
print("""Today I went to the zoo. I saw a(n)
___________(adjective)\n
_____________(Noun) jumping up and down in its tree.\n
He _____________(verb, past tense) __________(adverb)\n
through the large tunnel that led to its _______(adjective)\n
__________(noun). I got some peanuts and passed\n
them through the cage to a gigantic gray _______(noun)\n
towering above my head.\n""")
Adjective1 = input ("Please input the first adjective \n")
Noun1 = input ("Please input the first noun \n")
Verb1 = input ("Please input the first verb \n")
Adverb = input ("Please input the adverb \n")
Adjective2 = input ("Please input the second adjective \n")
Noun2 = input ("Please input the secod noun \n")
Noun3 = input ("Please input the third noun \n")
print("Today I went to the zoo. I saw a(n)"+Adjective1+"\n"+Noun1+"jumping up and down in its tree.\nHe"+Verb1+Adverb+"""\n
through the large tunnel that led to its"""+Adjective2+"\n"+Noun2+""". I got some peanuts and passed\n
them through the cage to a gigantic gray"""+Noun3+"\ntowering above my head.\n")