t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    cnt= 0
    for i in range(n):
        if(a[i]%2!=0):
            cnt +=1
    if(cnt%2!=0 or a[0]==1):
        print("CHEF")
    #elif(min(a[0],a[0]+n)!=1 and cnt%2==1):
        #print("CHEF")
    else:
        print("CHEFINA")    
