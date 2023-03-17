from typing import List


nums = [0,0,1,1,1,2,2,3,3,4]; 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        fi = 0; 
        mi = 0; 
        prev = nums[fi]

        for i in range(len(nums)):
            if i==0:
                continue; 

            if nums[i] != prev:
                fi+=1; 
                nums[fi] = nums[i]; 
                prev = nums[fi]

                
        

        return fi+1;   


sol = Solution(); 
count = sol.removeDuplicates(nums)   

print(count)