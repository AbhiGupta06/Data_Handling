# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:12:43 2019

@author: BSDU ADMIN
"""

N=int(input("Enter"))
X=int(input("Enter"))

def power(X,N):

   if N==0:
       return 1
   elif N%2==0:
        temp=power(X,int(N/2))
        return(power(X,int(N/2))*power(X,int(N/2)))
        return(temp * temp)
   else:
         #return(X*temp*temp)
        return(X*power(X,int(N/2))*power(X,int(N/2)))
        
 print(temp * temp)
print(power(X,N))

print("powewr of",X,"to",N,"is",power(X,N))