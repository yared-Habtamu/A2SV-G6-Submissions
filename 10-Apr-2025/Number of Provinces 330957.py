# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        if not isConnected: 
            return 0
        seen = set()
        def dfs(i):
            for q, adj in enumerate(isConnected[i]):
                if adj==1  and q not in seen:
                    seen.add(q)
                    dfs(q)
        s = len(isConnected)
        count = 0
        for i in range(s):
            if i not in seen: 
                dfs(i)
                count += 1
        return count
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        