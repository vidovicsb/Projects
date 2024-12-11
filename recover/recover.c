#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>


//TODO
int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if(card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t buffer[512];
    int numOfFiles = 0;
    char filename[8];
    bool found_jpg = false;
    FILE *img = NULL;

    while(fread(buffer, 1, 512, card) == 512)
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xff) == 0xe0)
        {
            found_jpg = true;
        }
        if(found_jpg == true)
        {
            if(numOfFiles == 0)
            {
                sprintf(filename, "%03i.jpg", numOfFiles);
                img = fopen(filename, "w");
                fwrite(buffer, 1, 512, img);
                numOfFiles++;
                found_jpg = false;
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", numOfFiles);
                img = fopen(filename, "w");
                fwrite(buffer, 1, 512, img);
                found_jpg = false;
                numOfFiles++;
            }
        }
        else if(numOfFiles != 0)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    fclose(card);
    fclose(img);


    return 0;
}
