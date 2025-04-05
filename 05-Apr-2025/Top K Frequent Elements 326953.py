# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        return sorted(freq_dict, key = lambda x: -freq_dict[x])[:k]

        # m = {}
        # r = []
        # for n in nums:
        #     if n in m:
        #         m[n] += 1
        #     else:
        #         m[n] = 1
        # print(m)
        # for j in range(k):
        #     max_freq = 0
        #     max_freq_num = 0
        #     for key, value in m.items():
        #         if value > max_freq:
        #             max_freq = value
        #             max_freq_num = key
        #     r.append(max_freq_num)
        #     m.pop(max_freq_num)
        # print(m)

        # return r
        







        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        