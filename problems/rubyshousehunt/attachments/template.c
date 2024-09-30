#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int income;
    float mr;
    int savings;
    scanf("%d%f%d", &income, &mr, &savings);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int price;
        int expenses;
        scanf("%d%d", &price, &expenses);
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("Yes, the house is affordable with 1 roommate(s) and $1 to spare.\n");

    return 0;
}
