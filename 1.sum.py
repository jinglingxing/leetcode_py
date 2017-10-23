# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:59:45 2017

@author: Jinling
"""

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return False
        myMap={}
        for i in range(len(nums)):
            if nums[i] in myMap:
                return [myMap[nums[i]],i]
            else:
                myMap[target- nums[i]]=i