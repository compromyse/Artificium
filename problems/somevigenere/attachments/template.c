#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char plain_text[64];
    scanf("%[^\n]", plain_text); fgetc(stdin);
    char key[64];
    scanf("%[^\n]", key);

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("Caesar would be proud\n");

    return 0;
}
