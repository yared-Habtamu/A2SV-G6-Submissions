# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums=[]
        def dfs(node,s):
            nonlocal nums
            if not node:
                return
            s+=(str(node.val))
            if not node.left and not node.right:
                nums.append(s)
                return

            dfs(node.right,s)
            dfs(node.left,s)

        dfs(root,"")
        tot=0
        # print(nums)
        for num in nums:
            tot+=(int(num))
        return tot