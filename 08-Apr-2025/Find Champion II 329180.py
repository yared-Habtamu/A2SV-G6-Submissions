# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDeg=[0]*n
        for i,j in edges:
            inDeg[j]+=1
        cnt=0
        val=-1
        for i in range(n):
            if inDeg[i]==0:
                val=i
                cnt+=1
        if cnt>1:
            return -1
        return val
        