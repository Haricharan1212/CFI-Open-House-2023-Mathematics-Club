import random       #importing the random module to simulate random events
import matplotlib.pyplot as plt   #importing the pyplot module of matplotlib to plot the graph
import numpy as np   #importing numpy module to use mathematical functions

num_trials = 1000  #number of trials for the simulation
n_values = list(range(1, 101)) #list of values of n from 1 to 100
proportions = []   #empty list to store the proportions of even splits for different n

for n in n_values:  # loop over all values of n
    num_even_splits = 0   #counter for number of even splits for current value of n
    for i in range(num_trials): # loop over num_trials simulations
        heads = 0   #counter for number of heads
        tails = 0   #counter for number of tails
        for j in range(2*n):     # toss 2*n coins
            if random.randint(0, 1) == 0:   # randomly choose between head and tail
                heads += 1
            else:
                tails += 1
        if heads == tails:   # check if the number of heads and tails is the same
            num_even_splits += 1   #increment the counter if an even split occurs
    proportion = num_even_splits / num_trials   #calculate the proportion of even splits for the current value of n
    proportions.append(proportion)   #append the proportion to the list

plt.plot(n_values, proportions)# plot the graph for proportion of even splits vs n
plt.xlabel("n")
plt.ylabel("Probability of even split")
plt.title("Probability of even split for n = 1 to 100")

# calculate the probability for large n using a formula
n = np.arange(1, 101)   #array of values of n from 1 to 100
calculated_probability = (np.pi * n)**(-1/2)   #calculate the probability using the formula

plt.plot(n_values, calculated_probability, label="Theoretical")# plot the graph for calculated probability vs n
plt.plot(n_values, proportions, label="Simulation")# plot the graph for proportion of even splits vs n
plt.xlabel("n")
plt.ylabel("Probability of even split")
plt.title("Probability of even split for n = 1 to 100")
plt.legend()
plt.show()   #display the plot
