def solution(arr, processes):
    answer = []
    current_time = 1
    current_work = 1 # read = 1 / write = 2
    delay_write = []
    delay_read = []
    for t in range(len(processes)):
        work = processes[t].split()
        w, t1, t2, a, b = work[0], int(work[1]), int(work[2]), int(work[3]), int(work[4])
        if t1 <= current_time:
            if  w == 'read' and current_work == 1: # 읽기 중 읽기 요청 = 동시 가능
                print('read')
                current_time = max(t1 + t2, current_time)
                answer.append(''.join(s for s in arr[a:b+1]))
            else: # 쓰기 작업 중이거나 읽기 중 쓰기 요청 = 동시 불가
                print('write')
                if w == 'read':
                    delay_read.append(processes[t])
                else:
                    delay_write.append(processes[t])
                current_work = 2
        else :
            print('delay')
            for d in delay_write:
                write = d.split()
                wt1, wt2, wa, wb, wc = int(write[1]), int(write[2]), int(write[3]), int(write[4]), write[5]
                current_time += wt2
                for x in range(wa, wb+1):
                    arr[x] = wc
            if current_time >= t1: # 작업중 뒤에 요청 또 들어오면
                if w == 'read':
                    delay_read.append(processes[t])
                else:
                    delay_write.append(processes[t])
            for d in delay_read:
                read = d.split()
                rt1, rt2, ra, rb = int(read[1]), int(read[2]), int(read[3]), int(read[4])
                current_time += rt2
                answer.append(''.join(s for s in arr[ra:rb+1]))

    print(current_time)
    return answer




arr = ["1", "2", "4", "3", "3", "4", "1", "5"]
processes = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]


# arr = ["1", "1", "1", "1", "1", "1", "1"]
# processes = ["write 1 12 1 5 8", "read 2 3 0 2", "read 5 5 1 2", "read 7 5 2 5", "write 13 4 0 1 3", "write 19 3 3 5 5", "read 30 4 0 6", "read 32 3 1 5"]
print(solution(arr, processes))