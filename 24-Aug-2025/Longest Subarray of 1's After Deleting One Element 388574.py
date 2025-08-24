# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution(object):
    def longestSubarray(self, nums):
        slow, fast = 0, 0
        max_len = 0
        zero_count = 0

        for fast in range(len(nums)):
            if nums[fast] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[slow] == 0:
                    zero_count -= 1
                slow += 1

            max_len = max(max_len, fast - slow)
            print(max_len)

        return max_len