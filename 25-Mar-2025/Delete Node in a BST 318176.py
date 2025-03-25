# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def left_most(node):
            cur=node
            while cur.left:
                cur=cur.left
            return cur
        if not root:
            return root
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                leftmost=left_most(root.right)
                root.val=leftmost.val
                root.right=self.deleteNode(root.right,leftmost.val)
        return root