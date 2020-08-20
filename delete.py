from math import sqrt,ceil,floor
N=int(input())
arr = [int(x) for x in input().split()]
arr.sort()
local = floor(1+sqrt(8*N+1))//2
print(local-1)