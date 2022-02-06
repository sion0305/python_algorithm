num_list = list(map(int, input().split()))
num_list.sort()

num_set = set(num_list)

if len(num_set) == 1:
    print(10000 + num_list[0] * 1000)
elif len(num_set) == 2:
    print(1000 + num_list[1] * 100)
else:
    print(num_list[2] * 100)

