#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
#Taking input from user
n = int(input("Enter number of digits in sequence:"))
seq = []
print("Enter sequence:")
for i in range(n):
    x = int(input(""))
    seq.append(x)
it = int(input("Enter number of iterations: "))
die = list(range(1, 7))
timer = []


def exp(n, seq, it):
    #Checks if the required sequence has been obtained
    def game_over_checker():
        c = 0
        for k in range(1, n+1):
            if throws[len(throws) - k] != seq[n - k]:
                c += 1
        if c == 0:
            return True
        else:
            return False

    throws = []
    #Finding the number of turns required 'it' times
    for i in range(it):
        #Atleast n turns will be required
        for j in range(n):
            throws.append(random.choice(die))
        #Count of number of turns
        counter = n
        #Keep throwing the dice until the required sequence is obtained.
        while game_over_checker() == False:
            throws.append(random.choice(die))
            counter += 1
        timer.append(counter)
    throws.clear()
    #Finding the average number of throws
    time_avg = sum(timer) / it
    timer.clear()
    print(time_avg)


print("The expected number of turns to get the required sequence are:")
exp(n ,seq, it)


# In[ ]:




