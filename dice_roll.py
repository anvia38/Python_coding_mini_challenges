#idea: use random.randint to make the rolls and use a for loop for 100 times. make a count variable for numbers 1-6, and use if and elif for each time random gets that number.
import random
from collections import defaultdict
import matplotlib.pyplot as plt
def diceRoll():
 
 
    """generates a random number from 1-6, 100 times
    and tells how  many times each number appeared"""


    # count1 = 0
    # count2 = 0 
    # count3 = 0 
    # count4 = 0
    # count5 = 0
    # count6 = 0
    # {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    d = defaultdict(int)
    print(d[0]) # regular dict would throw an error, this one gives 0
    
    data = []

    for _ in range(100):
        diceRoll = random.randint(1,6)
        data.append(diceRoll) 
        # if diceRoll == 1:
        #     count1 = count1+1
        d[diceRoll] += 1 # handles all the values in one
    
    print([f"Rolled {i} {d[i]} times" for i in [1,2,3,4,5,6]])
    plt.hist(data, bins = 6, rwidth=0.5, align='mid') # , color=['r','g','b','y','k','r']
    plt.show()

diceRoll()

 
