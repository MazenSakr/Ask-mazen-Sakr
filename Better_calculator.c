/*
|Author : Mazen Sakr
|File  Name : Better Calculator
|Description :-
*/

//  Includes section
#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)
/*********************/

void main(void) {
    system("color 30");
    float number1, number2;
    char Operator;
    printf("This is a calculator\nPlease input the first number : ");
    scanf(" %f",&number1);
    printf("\nPlease input the second number :");
    scanf(" %f",&number2);
    printf("\nPlease input the operator :");
    scanf(" %c",&Operator);
    switch (Operator) {
    case '+' :
        printf("\nThe sum is : %f", number1 + number2);
    break;
    case '-' :
        printf("\nThe difference is : %f", number1 - number2);
    break;
    case '*' :
        printf("\nThe product is : %f", number1 * number2);
    break;
    case '/' :
        printf("\nThe quotient is : %f", number1 / number2);
    break;
    default  :
        printf("\nInvalid operator.");
    break;
    }
}