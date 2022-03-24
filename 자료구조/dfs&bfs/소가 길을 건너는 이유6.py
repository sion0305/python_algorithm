from collections import deque

def solution():
    count = 0
    VECTOR = ((1, 0),(-1, 0),(0, 1),(0, -1))

    n, k, r = map(int, input().split())

    cow_matrix = [[0] * n for _ in range(n)]
    road_matrix = [ [ [] for _ in range(n) ] for _ in range(n) ]

    for _ in range(r):
        a, b, c, d = map(int, input().split())
        if road_matrix[a - 1][b - 1] == []:
            #print(road_matrix[a - 1][b - 1]==[])
            road_matrix[a - 1][b - 1] = [ [c-1, d-1] ]
        else:
            road_matrix[a - 1][b - 1].append([c-1, d-1])

        if road_matrix[c - 1][d - 1] == []:
            road_matrix[c - 1][d - 1] = [[a-1, b-1]]
        else:
            road_matrix[c - 1][d - 1].append([a-1, b-1])


    cow_list = list()
    cow_number = 0
    #여기서 EOF에러,,
    for _ in range(k):
        x, y = map(int, input().split())
        cow_matrix[x-1][y-1] = 1
        cow_list.append((x, y))
        cow_number += 1

    def bfs_cow(cow):
        now_count  = 0
        visited_matirx = [[0] * n for _ in range(n)]
        q = deque()
        q.append(cow)

        visited_matirx[cow[0]-1][cow[1]-1] = 1
        while q:

            now_xy = q.popleft()
            now_x = now_xy[0]
            now_y = now_xy[1]
            #print("now소",now_x,now_y)
            for (vec_x, vec_y) in VECTOR:
                #print(now_x -1 + vec_x, now_y -1  + vec_y, road_matrix[now_x-1][now_y-1])

                if 0 <= now_x - 1 + vec_x < n and 0 <= now_y - 1 + vec_y < n \
                    and visited_matirx[now_x-1 + vec_x][ now_y-1 + vec_y] != 1\
                        and (road_matrix[now_x-1][now_y-1] == [] or [now_x-1 + vec_x, now_y-1 + vec_y] not in road_matrix[now_x-1][now_y-1]):
                            q.append((now_x + vec_x, now_y + vec_y))
                            visited_matirx[now_x-1 + vec_x][now_y-1 + vec_y] = 1
                            #소를 만나면 카운트 증가
                            if cow_matrix[now_x-1 + vec_x][now_y-1 + vec_y] == 1:
                                now_count += 1
        return (cow_number - 1) - now_count

    for now_cow in cow_list:
        count += bfs_cow(now_cow)
        cow_matrix[now_cow[0] - 1][now_cow[1] - 1] = 0
        cow_number -= 1


    print(count)
