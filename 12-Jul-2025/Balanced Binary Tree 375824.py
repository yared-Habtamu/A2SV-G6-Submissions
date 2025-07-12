# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True,0]
            
            l_balance, l_height=dfs(root.left)
            r_balance, r_height=dfs(root.right)

            is_bal=abs(l_height-r_height)<=1 and l_balance and r_balance

            return [is_bal,1+max(l_height,r_height)]
        return dfs(root)[0]