from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums);  
        dict = {}; 

        cond = False; 
        for i in range(n):
            if nums[i] in dict:
                cond = True; 
                break; 
            else:
                dict[nums[i]] = 1;   

        return cond;   



