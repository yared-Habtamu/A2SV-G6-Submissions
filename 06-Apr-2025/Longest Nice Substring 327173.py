# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        sett=set(s)
        for i,char in enumerate(s):
            if char.swapcase() not in sett:
                sbefore = self.longestNiceSubstring(s[:i])
                safter= self.longestNiceSubstring(s[i+1:])

                if len(sbefore)>=len(safter):
                    return sbefore
                else:
                    return safter

        return s            