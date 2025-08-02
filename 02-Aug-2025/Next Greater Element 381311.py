# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for num in nums1:
            ind=nums2.index(num)
            if num==max(nums2) or ind==len(nums2)-1:
                ans.append(-1)
            else:
                for i in range(ind,len(nums2)):
                    if nums2[i]>num:
                        ans.append(nums2[i])
                        break
                else:
                    ans.append(-1)
        return ans
