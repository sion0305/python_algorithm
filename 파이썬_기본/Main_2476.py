n = int(input())
answer = 0
for i in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort()

    num_set = set(num_list)

    if len(num_set) == 1:
        answer = max(answer, 10000 + num_list[0] * 1000)
    elif len(num_set) == 2:
        answer = max(answer, 1000 + num_list[1] * 100)
    else:
        answer = max(answer, num_list[2] * 100)
    
print(answer)