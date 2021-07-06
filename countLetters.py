#create a class 
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
    example= "coconut124345?//>"
    sol=Solution()
    output=sol.lettercount(example)
    print(output)

 