# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        def canwe(mid,candies):
            tot=0
            for candy in candies:
                tot+=(candy//mid) 
            return tot

        while l<=r:
            mid=(l+r)//2
            val=canwe(mid,candies)
            if val>=k:
                l=mid+1
            else:
                r=mid-1

        return r

        

