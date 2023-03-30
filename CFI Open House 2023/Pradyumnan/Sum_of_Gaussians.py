#This program is to show that the sum of Gaussians is also a Gaussian.

import random as r
import math as m
from matplotlib import pyplot as plt

#the typical form of the PDF Gaussian variable is f(x) = (1/(c*(2pi)**0.5))*e^-((x-b)^2/2c^2)

def convolution(b1,c1,b2,c2):  #p1 and p2 are PDFs of two Gaussian variables. This function will convolute and plot the result.
    '''p1 = (1/(c1*(2*m.pi)**0.5))*m.exp(-(((x-b1)**2)/(2*c1**2)))
    b1 and c1 are the mean and standard deviation for the first PDF
    p2 = (1/(c2*(2*m.pi)**0.5))*m.exp(-(((x-b2)**2)/(2*c2**2)))
    b2 and c2 are the mean and standard deviation for the second PDF'''

    final = [0 for i in range(-40, 40)]  #we will be using -40 to +40 everywhere as we want x-axis to be in that range

    for i in range(-40,40):  #this loop is to find an array of value of the final PDF
        for j in range(-150,150):  #this loop is to find a specific value of the final PDF. Higher range gives better approximations
            x=j/10  #we define a new variable x so that the control variable j can remain an integer
            p1 = (1/(c1*(2*m.pi)**0.5))*m.exp(-((x-b1)**2)/(2*c1**2))
            p2 = (1/(c2*(2*m.pi)**0.5))*m.exp(-((i-x-b2)**2)/(2*c2**2))
            final[i+40] += p1*p2*0.1  #using the convolution formula and dx=0.1 #we are using i+40 as indexing must be non-negative

    x_axis = [0 for i in range(-40,40)]

    for k in range(-40,40):
        print(k, final[k+40],"\n")  #we use k+40 to make sure the indexing is non-negative
        x_axis[k+40]=k  #we use k+40 to make sure the indexing is non-negative

    plt.plot(x_axis,final,label="V1+V2")


pdf1 = [0 for l in range(-40,40)]
pdf2 = [0 for l in range(-40,40)] #we are using -40 to +40 as the critical case is when both b1 and b2 are +/-10
                                  #this way, we can keep the peak of the curve away from the edges of the graph

b1 = r.uniform(-10,10)
c1 = r.uniform(5,10)  #we are using thsi particular range of standard deviations as to make the graph appear smoother
b2 = r.uniform(-10,10)
c2 = r.uniform(5,10) #note that b1 and b2 are means and c1 and c2 are the standard deviations of two random variables
print (b1,c1,b2,c2)

for j in range(-40,40):
    pdf1[j+40]=(1/(c1*(2*m.pi)**0.5))*m.exp(-(j-b1)**2/(2*c1**2))
    pdf2[j+40]=(1/(c2*(2*m.pi)**0.5))*m.exp(-(j-b2)**2/(2*c2**2))
    print (j, pdf1[j+40],"\n",j,pdf2[j+40])  #we are using j+40 everywhere to avoid negative indices

x_axis = [k for k in range(-40,40)]

#given below is the theoretically obtained expression(y) for the PDF of the sum of the two variables

b=b1+b2
c=(c1**2 + c2**2)**0.5
y=[0 for l in range(-40,40)]
x_axis1=[l for l in range(-40,40)] #we are using a different set of x-values so that
                                   #one can see that the numerically obtained sum is ridiculously accurate

for j in range(-40,40):
    y[j+40]=(1/(c*(2*m.pi)**0.5))*m.exp(-(j-b)**2/(2*c**2))  #we use j+40 to avoid negative indexing. y represents the theoretical sum

plt.plot(x_axis,pdf1,label="Variable 1 (V1)")
plt.plot(x_axis,pdf2,label="Variable 2 (V2)")
convolution(b1,c1,b2,c2)
plt.plot(x_axis1,y,label="Theoretical Sum")
plt.xlabel("X-axis (Value)")
plt.ylabel("Y-axis (Probability Density)")
plt.legend()
plt.show()