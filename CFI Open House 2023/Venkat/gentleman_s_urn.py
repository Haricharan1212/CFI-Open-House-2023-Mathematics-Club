import random
import matplotlib.pyplot as plt
import numpy as np

def actualresult(b, r):
    """Calculate the actual probability of winning for the first player using mathematical result"""
    n = 1
    d = 1
    prob = 0
    k = r / (r + b)
    while True:
        prob += n / d
        n *= b * (b - 1)
        d *= (b + r - 1) * (b + r - 2)
        if d == 0 or b <= 0 or r == 0:
            break
        b -= 2
    return prob * k

def monte(black, red, num_simulations):
    """Simulate the game using Monte Carlo analysis"""
    num_win = 0     
    for i in range(num_simulations):
        urn = ['B'] * black + ['R'] * red       # create ballbag
        random.shuffle(urn)                     # shuffle the urn
        for j in range(len(urn)):
            if urn[j] == 'R':
                if (j) % 2 == 0:                # Person 1 wins
                    num_win += 1
                    break
                else:                           # Person 2 wins
                    break
    return num_win / num_simulations            # return the probability of winning for 1st person

def plotter(blackballs):
    """Plot the probability of winning for the first player using both Monte Carlo analysis and mathematical result"""
    x = np.zeros(blackballs+1)
    y = np.zeros(blackballs+1)
    z = np.zeros(blackballs+1)
    for i in range(blackballs+1):
        x[i] = i                      # Values for x plot
        y[i] = monte(i,1,9000)        # Values for y plot of Monte Carlo simulation values
        z[i] = actualresult(i,1)      # Values for y plot of theoretical result values
    plt.plot(x, y, label='Monte Carlo Method')
    plt.plot(x, z, label='Theoretical Result')
    plt.xlabel('Number of black balls in the urn')
    plt.ylabel('Probability of 1st player winning')
    plt.title("Gentleman's Urn")
    plt.legend()
    plt.ylim(0.3, 1.1)
    plt.show()

# Example usage
b = 4  # number of black balls
r = 1  # number of red balls
num_simulations = 100000
p = monte(b, r, num_simulations)
q = actualresult(b, r)
print("If Person starts:\n Monte Carlo analysis: {:.5f}\n Calculated probability: {:.5f}\n".format(p, q))

plotter(40)  # Plot the probability of winning for up to 40 black balls

#Venkat A