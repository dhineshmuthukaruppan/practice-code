# from collections import defaultdict
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hash_table = defaultdict(int)
#         for i in nums:
#             hash_table[i] += 1
        
#         for i in hash_table:
#             if hash_table[i] == 1:
#                 return i



# if we take xor or zero and some bit, it will return that bit
# if we take xor or two same bits,it will return 0
# we can xor all bits together to find the unique number


# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = 0
#         for i in nums:
#             a ^= i
#         return a