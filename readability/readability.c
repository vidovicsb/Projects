#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    double L = (double)count_letters(text)/count_words(text) * (double)100;

    double S = (double)count_sentences(text)/count_words(text) * (double)100;

    int index = round((0.0588 * L) - (0.296 * S) - 15.8);

    /*printf("%f\n", L);
    printf("%i\n", count_letters(text));
    printf("%i\n", count_words(text));
    printf("%i\n", count_sentences(text));*/

    if(index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if(index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}


int count_letters(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            n++;
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            n++;
        }
    }
    return n;
}

int count_words(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            n++;
        }
    }
    return n + 1;
}

int count_sentences(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.')
        {
            n++;
        }
        else if (text[i] == '!')
        {
            n++;
        }
        else if(text[i] == '?')
        {
            n++;
        }
    }
    return n;
}