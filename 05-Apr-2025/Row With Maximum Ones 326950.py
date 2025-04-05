# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        maxx=0
        idx=0
        
        for r in range(row):
            count1=0
            for c in range(col):
                if mat[r][c]==1:
                    count1+=1
            if maxx<count1:
                idx=r
            maxx=max(maxx,count1)
        return [idx,maxx]
