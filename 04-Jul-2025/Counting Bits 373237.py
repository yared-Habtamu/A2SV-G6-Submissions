# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            val=bin(i)
            count=Counter(val)
            ans.append(count['1'])
        return ans