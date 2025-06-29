# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        lo = 1
        hi = position[-1] - position[0]
        ans = 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.canWePlace(position, mid, m):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
    
    def canWePlace(self, arr, dist, balls):
        countBalls = 1
        lastPlaced = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
                if countBalls >= balls:
                    return True
        
        return False