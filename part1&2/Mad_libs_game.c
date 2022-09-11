/*
|Author : Mazen Sakr
|File  Name : Mad libs game
|Description :-
*/

//  Includes section
#include<stdio.h>
#include<stdlib.h>
/*********************/

void main(void) {
    system("color 30");
    char adjective1[20];
    char noun1[20];
    char verb1[20];
    char adverb[20];
    char adjective2[20];
    char noun2[20];
    char noun3[20];
    printf("This is a mad lips game \nfill in the blanks in the following text in order\nToday I went to the zoo.I saw a(n)___________(adjective)\n_____________(Noun) jumping up and down in its tree.\nHe _____________(verb, past tense) __________(adverb)\nthrough the large tunnel that led to its _______(adjective)\n__________(noun).I got some peanuts and passed\nthem through the cage to a gigantic gray _______(noun)\ntowering above my head.");
    printf("\nAdjective 1 is :");
    scanf("%s", &adjective1);
    printf("\nNoun 1 is :");
    scanf("%s", &noun1);
    printf("\nVerb 1 is :");
    scanf("%s", &verb1);
    printf("\nAdverb is :");
    scanf("%s", &adverb);
    printf("\nAdjective 2 is :");
    scanf("%s", &adjective2);
    printf("\nNoun 2 is :");
    scanf("%s", &noun2);
    printf("\nNoun 3 is :");
    scanf("%s", &noun3);
    printf("\nThe text is :\nToday I went to the zoo.I saw a(n) %s\n%s jumping up and down in its tree.\nHe %s %s\nthrough the large tunnel that led to its %s\n%s.I got some peanuts and passed\nthem through the cage to a gigantic gray %s\ntowering above my head.",adjective1,noun1,verb1,adverb,adjective2,noun2,noun3);
}