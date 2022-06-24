for _ in range(int(input())):
    n, x = map(int, input().split())
    p = int((10**9+7))
    sol = 1
    pop = 2
    y = n - 1
    pop = pop % p
    while y > 0:
        if y & 1:
            sol = (sol * pop) % p
        y = y >> 1
        pop = (pop * pop) % p
    losecal = (sol % p * x % p) % p
    print(losecal)