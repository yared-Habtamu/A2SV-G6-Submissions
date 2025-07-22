# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxx=0
        window=[]
        i=0
        j=0
        tot=0
        while i<len(nums):
            if nums[i] not in window or len(window)==0:
                window.append(nums[i])
                tot+=nums[i]
                maxx=max(maxx,tot)
                i+=1
            else:
                window.remove(nums[j])
                tot-=nums[j]
                j+=1
        return maxx
                