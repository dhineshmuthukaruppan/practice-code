from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}; 

        n = len(nums);    
        for i in range(n):
            complement = target - nums[i]

            if complement in hashmap: 
                return [i, hashmap[complement]];  

            hashmap[nums[i]] = i; 