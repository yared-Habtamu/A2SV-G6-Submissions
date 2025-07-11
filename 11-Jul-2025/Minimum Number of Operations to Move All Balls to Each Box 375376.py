# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        moves = 0 
        ops = 0    
        for i in range(n):
            ans[i] += ops
            if boxes[i] == '1':
                moves += 1
            ops += moves


        moves = 0
        ops = 0
        for i in range(n-1, -1, -1):
            ans[i] += ops
            if boxes[i] == '1':
                moves += 1
            ops += moves

        return ans
