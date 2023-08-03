import random
list1=[]
n=int(input("enter the number of numbers:"))

for i in range(n):
    x=random.randint(0,100)
    if x not in list1:     
     list1.append(x)   
print (list1)
    


    
      