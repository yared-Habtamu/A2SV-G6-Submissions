# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys
from collections import defaultdict, Counter

def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().split())
def read_list(): return list(map(int, sys.stdin.readline().split()))

def solve():
    n,k=read_ints()
    nums=read_list()

    ans=[]
    for i in range(1,n):
        ans.append(nums[i]-nums[i-1])
    ans.sort()

    print(sum(ans[:n-k]))

    

test_cases = 1
# test_cases = read_int()
for tc in range(test_cases):
    solve()