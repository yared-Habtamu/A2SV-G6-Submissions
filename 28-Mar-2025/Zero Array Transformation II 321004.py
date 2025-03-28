# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(k):
            l, r, val = queries[i]
            prefix[l] += val
            if r + 1 < n:
                prefix[r + 1] -= val

        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]

        return all(prefix[i] >= nums[i] for i in range(n))

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low, high, n = 0, len(queries), len(queries)
        ans = n + 1

        while low <= high:
            mid = (low + high) // 2
            if self.isZeroArray(nums, queries, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return -1 if ans > n else ans