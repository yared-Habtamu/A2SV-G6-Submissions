# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution(object):
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        # if len(nums)==1 and nums[0]==target:
        #     return 0
        while l <= h:
            mid = (l + h) // 2
            if nums[mid]==target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                h = mid-1
            # else:
            #     return mid
        return -1

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        