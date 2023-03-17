# nums: [1, 2, 3, 4, 5, 6]
# k: 2

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums);  
        k %= n;  

        start = count = 0; 

        while count < n:   
            current, prev = start, nums[start]; 
            
            while True:
                next_idx = (current + k)%n;   
                nums[next_idx], prev = prev, nums[next_idx];  

                current = next_idx;   

                count += 1; 

                if current == start:
                    break; 

            start +=1;   
    

## or we can use reverse technique

# class Solution:
#     def reverse(self, nums: list, start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1
                
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k %= n

#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)