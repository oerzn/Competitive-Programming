t = int(input())
for i in range(t):
    maxt,maxn,sumn = map(int,input().split())
    ans = 0
    while(maxt and sumn>0):
        maxt = maxt-1
        if(sumn>maxn):
            ans = ans + pow(maxn,2)
            sumn = sumn - maxn
        else:
            ans = ans + pow(sumn,2) 
            break
    print(ans)    