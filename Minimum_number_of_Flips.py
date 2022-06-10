t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = sum(a)
    if(k == 0):
        print(0)
    elif(k==1 or k ==-1):
        print(-1)
    elif(abs(k%2)!=0):
        print(-1)
    elif(k%2==0):
        print(round(k/2))
    
           
  