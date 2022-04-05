def solution(arr, brr):
    answer = 0
    success = [False for _ in range(len(arr))]
    while False in success:
        for i, size in enumerate(arr):
            if size == brr[i] or i == len(arr)-1:
                continue
            elif size > brr[i]:
                move = size - brr[i]
                size -= move
                arr[i+1] += move
            else:
                move = brr[i] - size
                if arr[i+1] - move < 1:
                    print('here')
                    continue
                size += move
                arr[i+1] -= move
            success[i] = True
            answer += 1
    return answer


arr = [3, 7, 2, 4]
brr = [4, 5, 5, 2]

arr = [2, 1, 6, 2]
brr = [3, 2, 4, 2]
print(solution(arr, brr))