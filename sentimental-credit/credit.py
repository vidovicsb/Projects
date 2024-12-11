def valid(num):
    sum = 0
    length = len(num)
    while length > 1:
        product = 2 * num[length - 2]
        for digit in str(product):
            sum += int(digit)
        length -= 2
    length = len(num)
    while length > 0:
        sum += num[length - 1]
        length -= 2
    if sum % 10 == 0:
        return True
    else:
        return False


def main():
    while True:
        try:
            number = int(input("Number: "))
            if number > 0:
                break
        except ValueError:
            print(end="")

    num = [int(x) for x in str(number)]

    if len(num) == 15:
        if num[0] == 3 and (num[1] == 4 or num[1] == 7):
            if valid(num) == True:
                print("AMEX")
                return
            else:
                print("INVALID")
                return
        else:
            print("INVALID")
            return

    elif len(num) == 16:
        if num[0] == 5 and (num[1] >= 1 and num[1] <= 5):
            if valid(num) == True:
                print("MASTERCARD")
                return
            else:
                print("INVALID")
                return

        elif num[0] == 4:
            if valid(num) == True:
                print("VISA")
                return
            else:
                print("INVALID")
                return

        else:
            print("INVALID")
            return

    elif len(num) == 13:
        if num[0] == 4:
            if valid(num) == True:
                print("VISA")
                return
            else:
                print("INVALID")
                return
        else:
            print("INVALID")
            return

    else:
        print("INVALID")
        return


main()
