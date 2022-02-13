n = int(input())

for i in range(n):
    p = int(input())
    max = 0
    mName = ""
    for j in range(p):
        price, name = input().split()
        price = int(price)
        if max < price:
            max = price
            mName = name
    print(mName)