n,m,k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

result = 0

while m > 0:
    for i in range(k):
        result += first
        m -= 1
    result += second
    m -= 1
    
print(result)