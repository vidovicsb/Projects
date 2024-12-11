#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char rotate(char c, int key);


int main(int argc, string argv[])
{
    if (argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for(int i = 0; i < strlen(argv[1]); i++)
    {
        if(isdigit(argv[1][i]) == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    string plain = get_string("plaintext:  ");
    printf("ciphertext: ");
    for(int i = 0; i < strlen(plain); i++)
    {
        printf("%c", rotate(plain[i], key));
    }
    printf("\n");


}

char rotate(char c, int key)
{
    if (c >= 65 && c <= 90)
    {
        c -= 65;
        c = ((c + key) % 26);
        c += 65;
        return c;
    }
    else if (c >= 97 && c <= 122)
    {
        c -= 97;
        c = ((c + key) % 26);
        c += 97;
        return c;
    }
    else
    {
        return c;
    }

}