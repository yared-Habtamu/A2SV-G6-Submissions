# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        ans=[]
        count=Counter(nums)
        for key,val in count.items():
            if val>1:
                ans.append(key)

        for i in range(1,len(nums)+1):
            if nums[i-1]!=i and i not in nums:
                ans.append(i)
                break
        return ans
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        