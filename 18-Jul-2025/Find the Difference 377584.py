# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in set(t):
            if s.count(ch)!=t.count(ch):
                return ch
        return ''


        # tt=list(t)
        # ss=list(s)
        # for i in tt:
        #     if i not in ss:
        #         return i
        #     else:
        #         ss.remove(i)
                
        # return ''
   