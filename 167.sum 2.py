
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:58:20 2017
@author: Jinling
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #traversal the nums based on hash

        myMap={}
        
        for i in range(0: len(nums)):

            if  nums[i] in myMap:
                return [myMap[nums[i]],i+1]
            else:
                myMap[target-nums[i]]=i+1