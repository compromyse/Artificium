#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char teams[101];
    scanf("%[^\n]", teams); fgetc(stdin);
    char scores_1[201];
    scanf("%[^\n]", scores_1); fgetc(stdin);
    char scores_2[201];
    scanf("%[^\n]", scores_2);
    for (int i = 0; i < 2; i++) {

        // Write an answer using printf(). DON'T FORGET THE TRAILING \n
        // To debug: fprintf(stderr, "Debug messages...\n");

        printf("Team name: score minutes_leading\n");
    }

    return 0;
}
