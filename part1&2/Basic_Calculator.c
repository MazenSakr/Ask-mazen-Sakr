/*
|Author : MAzen Sakr
|File  Name : basic calculator
|Description :-
*/

//  Includes section
#include<stdio.h>
#include<stdlib.h>
/*********************/

void main (void){
    system ("color 30");
    float number1, number2;
    printf("This is a progam  that adds two numbers \nPlease input the two numbers separated by a space\n");
    scanf("%f",&number1);
    scanf("%f",&number2);
    printf("The sum is : %f",number1+number2);
}