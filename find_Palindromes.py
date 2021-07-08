''' 
input=str
output= boolean 
'''

#this code takes some input, and will check if it is a palindrome or not. (also, the code will rid the input of spaces, and uppercase and special characters.)
def checkPalindrome(input):
    # first, change the value of input to the stripped value
    
    eout = [e for e in input if e.isalnum()] # this list comprehension is the same as lines 10-13
    # eout = []
    # for e in input:
    #     if e.isalnum():
    #         eout.append(e)

    input = ''.join(eout).lower() # join the letters and ignore case

    # save the  input, then check if it is equal to the flipped version
    return input == input[::-1]
    #input.strip()

def main():
     input="tacocat"
     #checkPalindrome(input)
     answer=checkPalindrome(input)
     print (answer)
if __name__ == "__main__":
    main()
