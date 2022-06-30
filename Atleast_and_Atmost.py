t = int(input())
for i in range(t):
    N = int(input())
    k1 = list(map(int, input().split()))
    LPB = [0] * (N + 5)
    UPB = [0] * (N + 5)
    value = 0
    for i in range(N):
        b = N - k1[i]
        LPB[k1[i]] += 1
        UPB[k1[i]] += b
        value += b
    short = LPB
    for i in range(N, -1, -1):
        short[i] += short[i + 1]
    for i in range(N):
        y = value - UPB[i] + short[i + 1]
        x = short[i + 1]
        print(x, y)