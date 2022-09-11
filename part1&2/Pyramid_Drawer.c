/*
|Author : Mazen Sakr
|File  Name : Pyramid drawer
|Description :-
*/

//  Includes section
#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)
/*********************/

void main(void) {
	int height = 0;
	printf("This is a program that draws a pyramid according to input height\nPlease input a height between 2 and 5:");
	while (1) {
		scanf("%d", &height);
		if (height >= 2 && height <= 5) break;
		else {
			printf("\nInvalid input\nPlease input a height between 2 and 5 :");
		}
	}
	for (int counter0 = 0; counter0 < height; counter0++) {
		for (int counter1 = 0; counter1 < height - counter0 - 1; counter1++) {
			printf(" ");
		}
		printf("/");
		for (int counter2 = 0; counter2 < counter0; counter2++) {
			printf("  ");
		}
		printf("\\\n");
	}
		for (int counter3 = 0; counter3 < height*2; counter3++) {
			printf("_");
		}
}