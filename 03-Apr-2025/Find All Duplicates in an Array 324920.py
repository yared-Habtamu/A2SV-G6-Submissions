# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        count=Counter(nums)
        ans=[]
        for key,value in count.items():
            if value>1:
                ans.append(key)
        return ans


















        # d = {}
        # for i in range(1, len(nums)+1):  
        #     d[i] = 0
        # for i in nums:
        #     d[i] += 1
        # result = []
        # for key, val in d.items():
        #     if val == 2:
        #         result.append(key)
        # return result   



        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        