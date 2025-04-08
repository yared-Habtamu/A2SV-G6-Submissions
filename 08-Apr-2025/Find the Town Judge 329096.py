# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        totrust=[0]*(n+1)
        trustedby=[0]*(n+1)

        for fromm,to in trust:
            totrust[fromm]+=1
            trustedby[to]+=1

        for num in range(1,n+1):
            if trustedby[num]==n-1 and totrust[num]==0:
                return num
        return -1














        # trust_counts = [0] * (n + 1)
        # trusts_others = [0] * (n + 1)
        
        # for a, b in trust:
        #     trusts_others[a] += 1
        #     trust_counts[b] += 1
        
        # for person in range(1, n + 1):
        #     if trust_counts[person] == n - 1 and trusts_others[person] == 0:
        #         return person
        
        # return -1
