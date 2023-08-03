list=[]
list2=[]
print("enter numbers of list:")
while True:
    x= int(input())
        
    if x ==0:
        break

    list.append(x) 
    list2.append(x)   

print(list)    
list2.sort() 

if (list==list2):
     print("The list is sorted")
else:
     print("The list is not sorted")



 
   

