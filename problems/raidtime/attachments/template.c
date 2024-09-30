#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int w;
    scanf("%d", &w); fgetc(stdin);
    for (int i = 0; i < w; i++) {
        char wall[257];
        scanf("%[^\n]", wall); fgetc(stdin);
    }
    int d;
    scanf("%d", &d); fgetc(stdin);
    for (int i = 0; i < d; i++) {
        char door[257];
        scanf("%[^\n]", door); fgetc(stdin);
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("0 C4 needed to go through 0 walls\n");

    return 0;
}
