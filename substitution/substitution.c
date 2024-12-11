#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

void sub(string pl, string cipher);
char abc[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};


int main(int argc, string argv[])
{

    int count = 0;


    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        count++;
        if(!(isalpha(argv[1][i])))
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }

        for(int j = i+1; j < strlen(argv[1]); j++)
        {
            if(argv[1][i] == argv[1][j])
            {
                printf("Key must contain 26 characters\n");
                return 1;
            }
        }
    }
    if (count != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string plain = get_string("plaintext: ");
    printf("ciphertext: ");

    sub(plain, argv[1]);

    printf("\n");
    return 0;





}

void sub(string pl, string cipher)
{
    int pos;
    for (int i = 0; i < strlen(pl); i++)
    {
        if (isupper(pl[i]))
        {
            pos = pl[i] - 65;
            pl[i] = toupper(cipher[pos]);
        }
        if (islower(pl[i]))
        {
            pos = pl[i] - 97;
            pl[i] = tolower(cipher[pos]);
        }
    }
    printf("%s", pl);
}