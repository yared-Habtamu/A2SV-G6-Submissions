# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber-=1  
            rem=columnNumber % 26
            ans=chr(65 + rem) + ans
            columnNumber//=26
        return ans
