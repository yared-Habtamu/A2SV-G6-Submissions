# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        r=0
        c=col-1
        while r<row and c>=0:
            if matrix[r][c]<target:
                r+=1
            elif matrix[r][c]>target:
                c-=1
            else:
                return True
        return False



    #     target_row=[]
    #     # for row in matrix:
    #     #     if row[0]<=target and row[-1]>=target:
    #     #         target_row=row
    #     #         break
    #     start=0
    #     end=len(matrix)*len(matrix[0])-1
        
    #     l=0
    #     r=len(target_row)-1
    #     while l<=r:
    #         mid=(l+r)//2
    #         if target_row[mid]==target:
    #             return True
    #         elif target_row[mid]>target:
    #             r=mid-1
    #         else:
    #             l=mid+1
    #     return False
