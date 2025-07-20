# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        print(count)
        ans=0
        max_odd=0
        vals=[]
        for key, val in count.items():
            vals.append(val)
        vals.sort(reverse=True)
        first_odd=0
        for v in vals:
            if v%2==0:
                ans+=v
            elif first_odd==0:
                ans+=v
                first_odd=1
            else:
                ans+=(v-1)
        return ans