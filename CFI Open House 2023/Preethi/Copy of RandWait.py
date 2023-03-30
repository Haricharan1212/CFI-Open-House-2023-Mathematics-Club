import random

l=100000  #number of Monte-Carlo iterations 


cnt=[0]*100 #how many times Person B chose rank "i" 


for k in range(l):
    
    n=[] #contains 100 random variables, later arranged by rank
    
    for i in range(100):
        n.append(random.random()) #inserting random variables between 0 and 1
        
    n.sort() #sorting in ascending order
    x=random.random() #Person B chooses from the same random variable pool
    
    for i in range(100):
        if x<n[i]:
            cnt[i]+=1 #increase the ith position by 1 since that is the rank in this iteration
            break
        


file=open("expecwaittime.txt", "w")

for m in range(100):
    file.write(str(m+1)+'\t') #rank
    file.write(str(cnt[m])+'\n') #number of times the rank showed up in 100,000 Monte-Carlo experiments
    m+=1

    
file.close()
