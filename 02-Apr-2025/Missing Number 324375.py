# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i!=nums[i]:
                return i
        return n












        # n = len(nums)   
        # xor1 = 0
        # xor2 = 0
        # for i in range(n + 1):
        #     xor1 ^= i
        #     # print(xor1)
        # for num in nums:
        #     xor2 ^= num
        #     # print(xor1)
        # return xor1 ^ xor2