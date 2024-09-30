#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int number_of_rounds;
    scanf("%d", &number_of_rounds);
    for (int i = 0; i < number_of_rounds; i++) {
        char alice_sequence[4];
        char bob_sequence[4];
        char round_tosses[21];
        scanf("%s%s%s", alice_sequence, bob_sequence, round_tosses);
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("WINNER!\n");

    return 0;
}
