#BTW, do not enter any character other than a number in the input.

def reverseDigits(x):
    """
    :reverses digits 
    :of 32 bit int
    """
    x_str = str(x) # convert integer to a string
    # check if the first symbol is a negative
    make_minus = False
    if x_str[0] == '-':
        make_minus = True
        x_str = x_str[1:]

    if len(x_str) != 1:
        # remove trailing zeroes
        while x_str[-1] == '0':
            x_str = x_str[:-1]

        # reverse x_str here
        reversed = ""
        for i in range(len(x_str)):
            reversed = x_str[i] + reversed
        x_str = reversed

    #x_str = x_str[::-1]
    
    if make_minus:
        x_str = '-' + x_str

    x_str = int(x_str) # cast back to an int

    if x_str == x: 
        print ("This number is a palindrome")
    return x_str
 
x = int(input("enter a number: "))
s = reverseDigits(x)
print(x, s)


   