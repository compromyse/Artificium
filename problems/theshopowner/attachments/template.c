#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int d;
    scanf("%d", &d);
    int c;
    scanf("%d", &c);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int unit_cost;
        int unit_revenue;
        int quantity;
        scanf("%d%d%d", &unit_cost, &unit_revenue, &quantity);
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("answer\n");

    return 0;
}
