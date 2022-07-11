t = int(input())
for i in range(t):
    #n = int(input())
    a,b,c,d = map(int,input().split())
    if((abs(a-b)%2==0 and abs(c-d)%2==0) or (abs(a-b)%2!=0 and abs(c-d)%2!=0)):
        print("YES")
    else:
        print("NO")    