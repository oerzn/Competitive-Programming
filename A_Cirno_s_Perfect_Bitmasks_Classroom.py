t = int(input())
for i in range(t):
    x = int(input())
    binary1 = bin(x)[2:]
    if x == 1 or x == 2:
        print(3)
        continue
    if binary1.count("1") == 1:
        print(x+1)
    else:
        k = 0
        p = len(binary1)-1
        for i in range(p, -1, -1):
            if binary1[i] == '0':
                k += 1
            else:
                break
        print(2**k )

      