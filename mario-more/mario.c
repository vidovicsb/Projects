#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    int space;
    int i, j;
    int k = 0;
    int n, m;

    for (i = 1; i <= height; i++, k = 0, m = 0)
    {
        for (space = 0; space < height - i; space++)
        {
            printf(" ");
        }
        while (k != i)
        {
            printf("#");
            k++;
        }
        printf("  ");

        while (m != i)
        {
            printf("#");
            m++;
        }
        printf("\n");
    }



}
