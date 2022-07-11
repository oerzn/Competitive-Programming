t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    x1 = pow(2,a)-1
    print(x1*(x1-1))