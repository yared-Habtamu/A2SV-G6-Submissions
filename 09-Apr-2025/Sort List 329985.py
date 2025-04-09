# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        def divide(head):
            if not head or not head.next:
                return head, None
            slow=head
            fast=head
            prev=None
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=None
            # right_half=head
            return head, slow

        def merge(left,right):
            dummy=ListNode()
            tail=dummy

            while left and right:
                if left.val<right.val:
                    tail.next=left
                    left=left.next
                else:
                    tail.next=right
                    right=right.next
             
                tail=tail.next
      
            if left:
                tail.next=left
            else:
                tail.next=right
            return dummy.next


        left_list,right_list=divide(head)

        left_list=self.sortList(left_list)
        right_list=self.sortList(right_list)

        return merge(left_list, right_list)

