import numpy as np
def checker():
    number=int(input("Enter A Number To Check If It Is Amstrong Number : \n"))
    
    number=str(number)
    
    list=[]
    
    list+=[int(digit) for digit in number]
    
    power=len(list)
    
    armstrong=0
    
    for i in range(0,power):
    
        armstrong+=list[i]**power

    if armstrong==int(number):
   
       print(number,"Is An Armstrong Number")    
    else:
       print("No,",number,"Is Not An Armstrong")     
   

def finder():
     
 rg=int(input("Enter The Maximum Range Required:\n"))    
 arml=[]
 for number in range(rg):
    list=[]
            
   
    list+=[int(digit) for digit in str( number)]
        
    powern=len(list)
        
    
    armstrong=np.sum(np.power(np.array(list),powern))
    if armstrong==int(number):
    
       arml.append(number)
 print(arml)   
finder()
# checker()

