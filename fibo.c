#include <stdio.h>

int main(){
    int a = 1;
    int b = 1;
    int c = 0;
    printf("please input a number:");
    scanf("%d", &c);
    printf("input number is %d\n", c);
    printf("fibo %d number is %d\n", 1, a);
    printf("fibo %d number is %d\n", 2, b);
    for (int i = 3; i <= c; i++){
        int d = a + b;
        printf("fibo %d number is %d\n", i, d);
        a = b;
        b = d;
    }
    return 0;
}
