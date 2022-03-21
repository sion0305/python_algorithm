def getMaxTime(read):
    maxT = 0
    for r in read:
        maxT = max(maxT, int(r[2]))
    return maxT
def solution(arr, processes):
    answer = []
    current_time = 1
    time = 0
    current_work = 0 # 0: nothing, 1: read, 2: write
    delay_write, delay_read = [], []

    while len(processes) > 0:
        work = processes[0].split()
        # print(current_time)
        if current_time >= int(work[1]):
            if current_work == 0: # 첫 작업일때 바로 실행
                if work[0] == 'read':
                    current_time = max(current_time, int(work[1]) + int(work[2]))
                    answer.append(''.join(s for s in arr[int(work[3]):int(work[4])+1]))
                    current_work = 1
                else: # write
                    current_time += int(work[2])
                    for i in range(int(work[3]), int(work[4]) + 1):
                        arr[i] = work[5]
                    current_work = 2
            elif current_work == 1: # 읽기 작업 중
                if work[0] == 'read': # 동시가능
                    current_time = max(current_time, int(work[1]) + int(work[2]))
                    answer.append(''.join(s for s in arr[int(work[3]):int(work[4])+1]))
                else: # write # 대기 필요
                    delay_write.append(work)
                    current_work = 2
            elif current_work == 2: # 쓰기 작업 중
                if work[0] == 'read': # 대기
                    delay_read.append(work)
                else: # write # 대기
                    delay_write.append(work)
        else:
            flag = 0
            # print(delay_write)
            # print(delay_read)
            while len(delay_write) > 0:
                d = delay_write[0]
                wt1, wt2, wa, wb, wc = int(d[1]), int(d[2]), int(d[3]), int(d[4]), d[5]
                current_time += wt2
                for x in range(wa, wb+1):
                    arr[x] = wc
                del delay_write[0]
                if int(work[1]) <= current_time and flag == 0: # 작업 중 요청시간이 되면 대기
                    # print('put')
                    if work[0] == 'read':
                        delay_read.append(work)
                    else:
                        delay_write.append(work)
                    flag = 1
            max_time = getMaxTime(delay_read)
            current_time += max_time
            while len(delay_read) > 0:
                d = delay_read[0]
                rt1, rt2, ra, rb = int(d[1]), int(d[2]), int(d[3]), int(d[4])
                answer.append(''.join(s for s in arr[ra:rb+1]))
                del delay_read[0]
                if int(work[1]) <= current_time and flag == 0: # 작업 중 요청시간이 되면 대기
                    if work[0] == 'read':
                        delay_read.append(work)
                    else:
                        delay_write.append(work)
                    flag = 1
        del processes[0]

    print(current_time)
    return answer



# arr = ["1", "2", "4", "3", "3", "4", "1", "5"]
# processes = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]
arr = ["1", "1", "1", "1", "1", "1", "1"]
processes = ["write 1 12 1 5 8", "read 2 3 0 2", "read 5 5 1 2", "read 7 5 2 5", "write 13 4 0 1 3", "write 19 3 3 5 5", "read 30 4 0 6", "read 32 3 1 5"]
print(solution(arr, processes))