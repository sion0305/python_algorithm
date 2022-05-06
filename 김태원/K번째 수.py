import sys
# sys.stdin=open("김태원/input.txt", "rt")

T = int(input())

for t in range(T):
    N, s, e, k = map(int, input().split())
    numList = list(map(int, input().split()))
    numList = numList[s-1:e]
    numList.sort()
    # numList = sorted(numList)
    # print('#',t+1,numList[k-1])
    print("#%d %d" %(t+1, numList[k-1]))