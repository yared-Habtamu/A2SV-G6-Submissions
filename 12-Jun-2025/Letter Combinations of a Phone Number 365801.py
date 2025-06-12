# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        DIGITS = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z")
        }

        ln = len(digits)
        res = []
        def combine(letters, i):
            if len(letters) >= ln:
                res.append(letters)
                return

            next_digit = digits[i]
            for l in DIGITS[next_digit]:
                combine(letters+l, i+1)
        combine("", 0)
        return res