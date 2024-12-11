// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// Counter variable for function size()
int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *ptr = table[index];
    while(ptr != NULL)
    {
        if(strcasecmp(ptr -> word, word) == 0)
        {
            return true;
        }
        else
        {
            ptr = ptr -> next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if(strlen(word) == 1)
    {
        return toupper(word[0]) - 'A';
    }
    else
    {
        return ((toupper(word[0]) - 'A') * 26) + toupper(word[1]) - 'A';
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for(int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    FILE *dict = fopen(dictionary, "r");
    if(dict == NULL)
    {
        printf("Was not able to open\n");
        return false;
    }

    char buffer[45];

    while(fscanf(dict, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        if(n != NULL)
        {
            counter++;
        }
        if(n == NULL)
        {
            return false;
        }
        strcpy(n -> word, buffer);
        n -> next = table[hash(n -> word)];
        table[hash(n -> word)] = n;
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *temp;
    for(int i = 0; i < N; i++)
    {
        temp = table[i];
        while(table[i] != NULL)
        {
            temp = table[i] -> next;
            free(table[i]);
            table[i] = temp;
        }
    }
    return true;
}


