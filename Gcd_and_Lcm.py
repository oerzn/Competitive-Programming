


import math
def cpair(nt):
    cnt_no = 0
    a= []
    w = int(math.sqrt(nt))
    for i in range(1,w+1):
        bsur = nt-i*i
        b = int(math.sqrt(bsur))
        if b*b == bsur:
            a.append([i,b])
    b = []
    c = []
    for i in c:
        p = min(i[0],i[1])
        q = max(i[0],i[1])
        if i[0]==0 or i[1]==0:
            cnt_no += 1
        else:
            for j in range(1,q):
                a,b=j,a+p
                b=a+p
                g = math.gcd(a,b)
                l = (a*b//g)
                if(g+l)==q:
                    cnt_no+=2
    for i in a:
        if i not in b:
            c.append(i)
            b.append([i[1],i[0]])
    
    return cnt_no                






t = int(input())
for i in range(t):
    n = int(input())
    if n%2 == 0:
        print(cpair(n))
    else:
        print(0)    
