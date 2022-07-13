t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b1,c1,d1,e1,f1=0,0,0,0,0
    for i in range(n):
        if(a[i]==1):
            d1+=1
        else:
            if(a[i]==2):
                c1+=1
            e1+= a[i]
            f1+=1
            if(a[i]%2):
                b1+=1








    if(d1==1):
        k = (b1%2)
        print(k)
        if(k):
            print("CHEF")
            continue
        if(c1==0):
            print("CHEFINA")
            continue
        e1-=2
        f1-=1
        if((e-f)%2):
            print("CHEFINA")
            continue
        else:
            print("CHEF")
            continue






    elif(d1>1):
        if((e1-f1)%2):
            print("CHEF")
            continue
        else:
            print("CHEFINA")
            continue






    if(b1%2):
        print("CHEF")
        continue
    else:
        print("CHEFINA")
        continue



