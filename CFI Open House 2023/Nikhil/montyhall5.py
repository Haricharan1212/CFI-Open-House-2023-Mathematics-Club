# code for n doors monty hall
import matplotlib.pyplot as plt
import random
def montyhall(q,n,p):
  
 win =0
 count=0

 for l in range(n):
  list=[]
  list.append(1)
  for i in range(q-1):
   list.append(0)

  rem=[]
  rem1=[]
  k=0
  a= random.randint(0,q-1) # this is the random door chosen by the player initially
  for i in range(q):
    if i!=a and list[i]==0:
      rem.append(i)  #rem is a list of indices all the empty doors (other than the door chosen by the contestant initially) that the host can open.
      k+=1

 
  for i in range(q-p) :
     b=random.randint(0,k-1) # rem1 is the list of empty doors opened by the host
     rem1.append(rem[b])
     del rem[b]
     k-=1
  pos=[]
  size=0

 
 
 
  for i in range(q):
  
   if i!=a and (i in rem1) == False:
     pos.append(i)     #pos is the list of possible doors that the contestant can switch to 
     size+=1
  index=random.randint(0,size-1)
  #print(pos,index)
  if list[pos[index]]==1:
   win+=1
  count+=1
 
 return (win/count)*100
x=[]
y=[]
#q=int(input("enter no of doors"))
n=int(input("enter no of trials"))
p=int(input("enter no of empty doors to be opened by the host in the form n-x enter x(where n is the total no of doors)"))


for i in range(p,100,1):
  x.append(i)
  y.append(montyhall(i,n,p))

#print(y)
plt.plot(x,y,label="simulated values")
x=[]
y=[]
for i in range(p,100,1):
  x.append(i)
  y.append(((i-1)/i)*(100/(p-1)))
plt.plot(x,y,color='red',label= "expected values")
plt.xlabel('no of boxes')
plt.ylabel('percentage wins')
plt.legend()