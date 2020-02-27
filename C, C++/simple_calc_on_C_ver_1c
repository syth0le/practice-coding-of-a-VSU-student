/*
 ============================================================================
 Name        : simple_calc_on_C.c
 Author      : sythole
 Version     :
 Copyright   : my and only my
 Description : calc in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	float firstNum, secondNum, result, var1, var2;
	int ist0;
	int ist1;
	char sign = '+';
	while (sign != '#') {
	    printf("sign: ");
	    scanf("%c%*c", &sign);
        if (sign == '+' || sign == '-' || sign == '*' || sign == '/' || sign == '!' || sign == '^') {
            printf("input_firstNum=");
            scanf("%f%*c", &firstNum);
            printf("input_secondNum=");
            scanf("%f%*c", &secondNum);
            switch (sign) {
                case '+':
                    printf("%.2f\n", firstNum+secondNum);
                    break;
                case '-':
                    printf("%.2f\n", firstNum-secondNum);
                    break;
                case '*':
                    printf("%.2f\n", firstNum*secondNum);
                    break;
                case '/':
                    if (secondNum != 0) printf("%.2f\n", firstNum/secondNum);
                    else printf("mistake!U can't divide into 0\n");
                    break;
                case '!':
                    var1=0;
                    var2=1;
                    for (int ist1=1; ist1<=firstNum;ist1++){
                        var2 = var2 * ist1;
                        var1 = var2;}
                    printf("%.2f\n", var2);
                    break;
                case '^':
                    var2 = 1;
                    var1 = 1;
                    for (int ist1=1;ist1<=secondNum;ist1++){
                        var1 = var2;
                        var2 = var1 * firstNum;}
                    printf("%.2f\n", var2);
                    break;
                }
            }
        else if (sign == '#'){
            break;
        }
    else printf("can't understand this\n");
    }
}
