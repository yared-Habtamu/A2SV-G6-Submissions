# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def backt(s):
            nonlocal ans
            if n==len(s):
                subs=''.join(s)
                ans.append(subs)
                return 

            if not s or (s[-1]=='1'):
                s.append('0')
                backt(s)
                s.pop()
            s.append('1')
            backt(s)
            s.pop()

        backt([])

        return ans