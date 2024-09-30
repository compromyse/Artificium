#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char solution[6];
    scanf("%[^\n]", solution);
    int n;
    scanf("%d", &n); fgetc(stdin);
    for (int i = 0; i < n; i++) {
        char guess[6];
        scanf("%[^\n]", guess); fgetc(stdin);
    }
    for (int i = 0; i < n; i++) {

        // Write an answer using printf(). DON'T FORGET THE TRAILING \n
        // To debug: fprintf(stderr, "Debug messages...\n");

        printf("__G_Y\n");
    }

    return 0;
}
