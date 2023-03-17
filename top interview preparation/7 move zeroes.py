from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lastnonzero = 0; 
        n = len(nums)
        for cur in range(n):
            if nums[cur] != 0:
                nums[lastnonzero], nums[cur] = nums[cur], nums[lastnonzero]; 

                lastnonzero+=1; 

