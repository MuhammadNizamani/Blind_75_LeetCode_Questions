from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for  index ,value in enumerate(nums):
            # temp = x
            # for y in nums
            
            new_list = nums[index+1:]
            for ind , num in enumerate(new_list):
                if value+num == target:
                    # print(value, "location of value ==", index ,num , "Index of the num is  ==", index+ind+1)
                    return [index, index+ind+1]
            
        #     print("value =  ", value, "index = ", index)
        #     print(new_list)
        #     # print(index)
    
        # print("target",target)
        # print(new_list)   
            

sol = Solution()
list_sol = sol.twoSum(nums=[2,7,11,15], target=9)
print(list_sol)