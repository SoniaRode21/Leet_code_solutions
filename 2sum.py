'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)):
            find=(target-nums[i])
            if find in nums :
                if nums.count(find)>1:
                    return [i,nums.index(find,i+1)]
                else:
                    if nums.index(find)!=i:
                        return [i,nums.index(find)]
            
            
        
        