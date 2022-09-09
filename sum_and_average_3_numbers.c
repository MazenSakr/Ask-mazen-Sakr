/*
|Author : Mazen Sakr
|File  Name : Sum & Average of 3 numbers
|Description :-
*/

//  Includes section
#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)
/*********************/

void main(void) {
    system ("color 30");
    float number1, number2, number3;
    printf("This is a program that prints the sum and average of 3 numbers\nPlease input the 3 numbers separated by spaces:");
    scanf("%f", &number1);
    scanf("%f", &number2);
    scanf("%f", &number3);
    printf("The sum is %f,the average is%f", number1 + number2 + number3, (number1 + number2 + number3) / 3);
}