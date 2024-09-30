#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int iteration;
    scanf("%d", &iteration);
    int size;
    scanf("%d", &size); fgetc(stdin);
    for (int i = 0; i < size; i++) {
        char ROW[1025];
        scanf("%[^\n]", ROW); fgetc(stdin);
    }

    return 0;
}
