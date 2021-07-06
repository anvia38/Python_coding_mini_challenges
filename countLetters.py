#create a class 
#this will tell you how many unique letters are in a string of your choice. (it only tells you UNIQUE LETTERS)
class Solution(object):
    def lettercount(self, letter):
        ''' Counts the number of letters in a str
        input type: str input=letter
        output= int '''
        setv ="".join(set(letter))
        chr_codes = [ord(i) for i in setv]
        count = 0
        for c in chr_codes:
            if (65<=c and c<=90) or (97<=c and c<=122):

              count = count+1
        return count
        
        

if __name__=="__main__":
    example= "coconut124345?//>"# enter what you want your string to be.
    sol=Solution()
    output=sol.lettercount(example)
    print(output)

 
