# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
    new_str=''
    for digit in str(num):
        digit_as_int=int(digit)
        square_num=digit_as_int*digit_as_int
        new_str+=str(square_num)
    return int(new_str)

print(square_digits(9119))