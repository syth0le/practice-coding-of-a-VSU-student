/*
 ============================================================================
 Name        : my_f1rst_test.c
 Author      : Cat
 Version     :
 Copyright   : mya
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    float firstNum, secondNum, result, var1, var2;
    int ist0;
    int ist1;
    int turn_on = 1;
    char sign = '+';
    while(turn_on != 0){
        printf("type first number:");
        scanf("%f%*c", &firstNum);
        printf("sign: ");
        scanf("%c%*c", &sign);
        if (sign == '+' || sign == '-' || sign == '*' || sign == '/' || sign == '^'){
            printf("type second number:");
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
                case '^':
                    var2 = 1;
                    var1 = 1;
                    for (int ist1=1;ist1<=secondNum;ist1++){
                        var1 = var2;
                        var2 = var1 * firstNum;}
                    printf("%.2f\n", var2);
                    break;}
        }
        else if(sign == '!'){
            var1=0;
            var2=1;
            for (int ist1=1; ist1<=firstNum;ist1++){
                var2 = var2 * ist1;
                var1 = var2;}
            printf("%.2f\n", var2);}
        else printf("unsupportable sign. Please, type another from this range: +, -, *, /, ^, !.\n");
        printf("If u want to continue type 1, but if u want to exit type 0:");
        scanf("%i", &turn_on);
    }

}
