#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void main(void)
{
	srand(time(0));
	int guess=0, hotColdIndicator=3;
	int randomNumber =rand()%10;
	printf("This is a guessing game , if you can guess the right number between 0-9 with 4 or less attempts you win\n ");
	for (int counter=0;counter<4; counter ++)
{
    printf("\nWhat's your guess ?");
     scanf("%d",&guess);
     if (guess==randomNumber){
         printf("\nYou win!!");
         exit(0);
          }
      if (abs(guess-randomNumber)<hotColdIndicator ){
          printf("\nHotter");
          } else {
              printf("\nColder");
              }
              hotColdIndicator=abs(guess-randomNumber);
    }
    printf("\nOut of guesses.");
}