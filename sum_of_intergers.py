"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: int, target: int):
        if len(nums)<=1:
            return None
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
                
def verify(result):
    print("Indeces are: ", result)
       
my_list = [1,2,3,4,5,6,7]

my_object = Solution()


result = my_object.twoSum(my_list,12)

verify(result)

