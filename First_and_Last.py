t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if(len(a)==1):
        print(max(a))
    elif(len(a)==2):
        print(sum(a))
    else:
        res = [x + y for x, y in zip(a, a[1:] + [a[0]])]
        print(max(res))
        


