#include <math.h>
#include "helpers.h"

// Convert image to grayscale - TODO
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float avg;
    int avg_int;
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            avg_int = round(avg);
            image[i][j].rgbtRed = avg_int;
            image[i][j].rgbtGreen = avg_int;
            image[i][j].rgbtBlue = avg_int;
        }
    }
    return;
}

// Convert image to sepia - TODO
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            if(sepiaRed > 255)
                image[i][j].rgbtRed = 255;
            else
                image[i][j].rgbtRed = sepiaRed;

            if(sepiaGreen > 255)
                image[i][j].rgbtGreen = 255;
            else
                image[i][j].rgbtGreen = sepiaGreen;

            if(sepiaBlue > 255)
                image[i][j].rgbtBlue = 255;
            else
                image[i][j].rgbtBlue = sepiaBlue;

        }
    }
    return;
}

// Reflect image horizontally - TODO
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image - TODO
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            //TOP LEFT
            if(i - 1 < 0 && j - 1 < 0)
            {
                image[i][j].rgbtRed = round((temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed) / 4.0);
                image[i][j].rgbtGreen = round((temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue) / 4.0);
            }

            //TOP RIGHT
            else if(i == 0 && j == width - 1)
            {
                image[i][j].rgbtRed = round((temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed) / 4.0);
                image[i][j].rgbtGreen = round((temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue) / 4.0);
            }

            //BOTTOM LEFT
            else if(i == height - 1 && j == 0)
            {
                image[i][j].rgbtRed = round((temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed) / 4.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue) / 4.0);
            }

            //BOTTOM RIGHT
            else if(i == height - 1 && j == width - 1)
            {
                image[i][j].rgbtRed = round((temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed) / 4.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue) / 4.0);
            }

            else if(i - 1 < 0)
            {
                image[i][j].rgbtRed = round((temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue) / 6.0);
            }

            else if(j - 1 < 0)
            {
                image[i][j].rgbtRed = round((temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue) / 6.0);
            }

            else if(j + 1 == width)
            {
                image[i][j].rgbtRed = round((temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue) / 6.0);
            }

            else if(i + 1 == height)
            {
                image[i][j].rgbtRed = round((temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue) / 6.0);
            }

            else
            {
                image[i][j].rgbtRed = round((temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed) / 9.0);
                image[i][j].rgbtGreen = round((temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen) / 9.0);
                image[i][j].rgbtBlue = round((temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue) / 9.0);
            }
        }
    }
    return;
}
