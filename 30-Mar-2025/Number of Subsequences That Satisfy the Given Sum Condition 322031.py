# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        ans=0
        nums.sort()
        mod=1000000007
        while i<=j:
            if nums[i]+nums[j]>target:
                j-=1   
            else:
                ans=(ans+(pow(2,(j-i),mod)))%mod
                i+=1    
        return ans