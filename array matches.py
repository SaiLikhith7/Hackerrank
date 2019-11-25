# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:26:10 2019

@author: likki
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter=0
    d=int((n+1)/2)
    e=int((n+2)/2)
    for i in range(0,d):    
        for j in range(e,n):
            if(ar[i]==ar[j]):
                counter+=1
                print("ar[i]" + str(ar[i]))
                print("ar[j]" + str(ar[j]))
                
                print(counter)
                break
    return counter


if __name__ == '__main__':
    
    n = 9

    ar = [10,20,20,10,10,30,50,10,20]

    result = sockMerchant(n, ar)
    print(result)