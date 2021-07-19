
def findPrimeNum(x):
    """finds the number of prime numbers
    below the input"""

    # create a list where each entry corresponds to the index-valued number
    primes = [True] * x # if x = 10, primes = [True, True, ..., True]
    primes[0] = False # 0 is not prime
    primes[1] = False # 1 is not prime
    # 100 = (5x20), 10x10, (20x5)
    for i in range(2,int(x**0.5)+1):
        if primes[i] == True:
            for j in range(i*i, x, i): 
                # 2: 4, 6, 8, 10, ..., 100
                # 3: 9, 12, 15, 18, 21, 24, 27...
                # 4: skip
                # 5: 25 (5, 10, 15, 20...?)
                # 9 x N = 3 x (3 x N)
                primes[j] = False
    count = 0
    for prime in primes:         
        if prime == True:
            count = count+1
    
    return count

def main():
    test = 11# <-enter the number you want to find the number of primes below here
    output = findPrimeNum(test)
    print(output)

if __name__ == "__main__":
    main()
