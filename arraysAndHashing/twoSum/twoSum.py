from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in hashmap: 
                return [hashmap[diff], i]
            hashmap[n] = i
        return 
        
    
    
nums = [3,4,5,6]
target = 7
sol = Solution()
print(sol.twoSum(nums, target))
