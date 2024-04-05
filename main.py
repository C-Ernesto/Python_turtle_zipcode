# Name: Christopher Ernesto
# Lab 3 – Task 3
# This code will generate a US postal barcode from a zip code (in zip+4)

import PrintDigits


# remove dash from the zip code
def remove_dash(inputString):
    inputString = inputString.replace("-", "")  # replace all dash with an empty string
    return inputString


# calculate the check sum for the zip code
# the check sum is a number such that the addition of all the digits is a multiple of 10 (including the checksum)
# returns the checksum as a string to be easily concatenated
def calculate_checksum(code):
    sum = 0  # keep track of sum of digit

    # get each digit
    for digit in code:
        sum += int(digit)  # add each digit to the sum

    # get the digit that would make the sum of the digits a multiple of 10
    ret = 0  # variable to store check sum digit
    if (sum % 10) != 0:
        ret = 10 - (sum % 10)   # mod gives us remainder, and the digit necessary to get a multiple of 10 is 10 minus
                                # the remainder. Unless 0 where check digit is also 0 instead of 10

    # return check sum digit as string
    return str(ret)


# Function to get the encoded zip code
def get_encoded(zipCode):
    zipCode = remove_dash(zipCode)  # Removes the dash from the string
    zipCode = zipCode + calculate_checksum(zipCode)  # calculate and concatenate the checksum to the end of the code
    return zipCode


def main():
    zipCode = input("Enter a Zip+4 code: ")  # get zip code from user
    encodedCode = get_encoded(zipCode)  # get the encoded zip code
    print(encodedCode)

    # print starting symbol
    PrintDigits.print_start_stop()

    # get each digit in the encoded zip code
    # for each digit, tell turtle to draw the barcode
    for digit in encodedCode:
        digit = int(digit)  # convert digit from str to int
        if digit == 0:
            PrintDigits.print_zero()
        elif digit == 1:
            PrintDigits.print_one()
        elif digit == 2:
            PrintDigits.print_two()
        elif digit == 3:
            PrintDigits.print_three()
        elif digit == 4:
            PrintDigits.print_four()
        elif digit == 5:
            PrintDigits.print_five()
        elif digit == 6:
            PrintDigits.print_six()
        elif digit == 7:
            PrintDigits.print_seven()
        elif digit == 8:
            PrintDigits.print_eight()
        elif digit == 9:
            PrintDigits.print_nine()

    # print ending symbol
    PrintDigits.print_start_stop()

    PrintDigits.draw.exitonclick()  # don't close window when finished


if __name__ == '__main__':
    main()

