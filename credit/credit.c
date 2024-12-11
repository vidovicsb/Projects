#include <cs50.h>
#include <stdio.h>


bool valid(long n);


int main(void)
{

    long cardNumber = get_long("Number: ");

    if(cardNumber / 100000000000000 != 0 && ((cardNumber / 100000000000000 == 3 && (cardNumber / 10000000000000) % 10 == 4) || (cardNumber / 100000000000000 == 3 && (cardNumber / 10000000000000) % 10 == 7)))
    {

        if(valid(cardNumber) == true)
        {
            printf("AMEX\n");
        }
        else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
    }
    else if(cardNumber / 1000000000000000 == 4 && cardNumber / 10000000000000000 == 0)
    {
        if(valid(cardNumber) == true)
        {
            printf("VISA\n");
        }
        else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
    }
    else if(cardNumber / 1000000000000 == 4 && cardNumber / 10000000000000 == 0)
    {
        if(valid(cardNumber) == true)
        {
            printf("VISA\n");
        }
        else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
    }
    else if(cardNumber / 1000000000000000 == 5 && cardNumber / 10000000000000000 == 0)
    {
        if((cardNumber / 100000000000000) % 10 == 1)
        {
            if(valid(cardNumber) == true)
            {
            printf("MASTERCARD\n");
            }
            else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
        }
        else if((cardNumber / 100000000000000) % 10 == 2)
        {
            if(valid(cardNumber) == true)
            {
            printf("MASTERCARD\n");
            }
            else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
        }
        else if((cardNumber / 100000000000000) % 10 == 3)
        {
            if(valid(cardNumber) == true)
            {
            printf("MASTERCARD\n");
            }
            else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
        }
        else if((cardNumber / 100000000000000) % 10 == 4)
        {
            if(valid(cardNumber) == true)
            {
            printf("MASTERCARD\n");
            }
            else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }
        }
        else if((cardNumber / 100000000000000) % 10 == 5)
        {
            if(valid(cardNumber) == true)
            {
            printf("MASTERCARD\n");
            }
            else if(valid(cardNumber) == false)
            {
                printf("INVALID\n");
            }

        }
        else
        {
            printf("INVALID\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }


}



bool valid(long n)
{
    long number;
    long sum = 0;

    for(long i = 10; i <= 1000000000000000; i *= 100)
    {
        number = ((n / i) % 10) * 2;

        sum = sum + number / 10 + number % 10;

    }
    for(long i = 1; i <= 1000000000000000; i*= 100)
    {
        number = (n / i) % 10;
        sum = sum + number % 10;
    }

    if(sum % 10 == 0)
    {
        return true;
    }
    else if(sum % 10 != 0)
    {
        return false;
    }
    else
    {
        return false;
    }


}

