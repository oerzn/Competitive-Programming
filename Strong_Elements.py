from math import gcd as g  
def gcd(l, r, pfx, sfx):

    if l == 0: 
        return sfx[r + 1] 
    if r == len(arr) - 1: 
        return pfx[l - 1] 
    return g(pfx[l - 1], sfx[r + 1]) 

def fps(pfx, arr, sfx, n): 
      
    pfx[0],sfx[n - 1] = arr[0] , arr[n - 1]  
    for i in range(1, n): 
        pfx[i] = g(pfx[i - 1], arr[i]) 
    for i in range(n - 2, -1, -1): 
        sfx[i] = g(sfx[i + 1], arr[i]) 
  
def gosr(n): 
  
    pfx, sfx= [0] * n ,[0] * n   
    fps(pfx, arr, sfx, n) 
    ans = 0
    for i in range(n): 
          
        if gcd(i, i, pfx, sfx) > 1: 
            ans += 1
              
    return ans 

t = int(input()) 
  
for j in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 
    print(gosr(n))