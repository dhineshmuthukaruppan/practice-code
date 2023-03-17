from typing import List

input = [4,1,2,1,2]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sorted()

        nums.sort(); 

        # print(nums);   
        
        n = len(nums);   
        result = 0;  

        if n == 1:
            result = nums[0]; 
            return result; 


        for i in range(0, n):   
            if i == 0:
                if nums[i] != nums[i+1]:
                    result = nums[i]
                    break; 

            elif i == n-1:
                if nums[i] != nums[i-1]:
                    result = nums[i]
                    break; 
            else:
                if not ((nums[i] != nums[i+1] and nums[i] == nums[i-1]) or (nums[i] == nums[i+1] and nums[i] != nums[i-1])):
                    result = nums[i]; 
                    break; 


        return result;   


sol = Solution(); 

res = sol.singleNumber(input);   

# print(res);    




# from collections import defaultdict
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hash_table = defaultdict(int)
#         for i in nums:
#             hash_table[i] += 1
        
#         for i in hash_table:
#             if hash_table[i] == 1:
#                 return i


# 2∗(a+b+c)−(a+a+b+b+c)=c
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return 2 * sum(set(nums)) - sum(nums)



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