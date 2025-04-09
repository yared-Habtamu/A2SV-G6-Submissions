# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        l=0
        r=n-1
        res=l
        while l<=r:
            mid=(l+r)//2
            idx=n-mid
            if citations[mid]>=idx:
                res=idx
                r=mid-1
            else:
                l=mid+1
        return res