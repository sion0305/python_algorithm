from xmlrpc.client import boolean

# n의 홀짝 여부에 따라 규칙 적용
def howMany(n, i):
    if n % 2 == 0:
        if i % 2 == 0:
            i -= 1
        else:
            i -= 2
    else:
        if i % 2 == 0:
            i -= 2
        else:
            i -= 1
    return i if i > 0 else 1

def solution(n, clockwise):
    answer = [[1 for _ in range(n)] for _ in range(n)]

    # clockwise에 따른 방향 설정하기
    if clockwise == True:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        orders = [[0,0], [0,n-1], [n-1, n-1], [n-1,0]]
    else :
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        orders = [[0,0], [n-1,0], [n-1, n-1], [0, n-1]]

    # 소용돌이 시작점과 이동 방향 설정
    for idx in range(4):
        # 시작점
        startX, startY = orders[idx][0], orders[idx][1]
        # 이전 값
        pre = 1
        dirIdx = idx
        # 현재 방향으로 얼만큼 이동할건지
        i = n-2
        while i != 1:
            for j in range(i):
                # 방향에 맞게 이동
                startX += dirs[dirIdx][0]
                startY += dirs[dirIdx][1]
                # 이동에 따른 입력값 증가
                pre += 1
                answer[startX][startY] = pre
                print('start' ,startX, startY, pre)
                print('dir' , dirs[dirIdx][0], dirs[dirIdx][1])
                
            dirIdx = (dirIdx + 1) % 4
            # 다음 이동 횟수
            i = howMany(n, i)
        # 마지막 하나 이동 해야함
        startX += dirs[dirIdx][0]
        startY += dirs[dirIdx][1]
        # 이동에 따른 입력값 증가
        pre += 1
        answer[startX][startY] = pre

    return answer

n, clockwise = input().split()
print(solution(int(n), boolean(clockwise)))