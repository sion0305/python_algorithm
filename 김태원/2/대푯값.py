import sys
import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    print(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

sys.stdin=open("김태원/input.txt","rt")

n = int(input())

a = list(map(int, input().split()))

average = np.mean(a)
# print(average)

near = find_nearest(a, average)
print(near, a.index(near))