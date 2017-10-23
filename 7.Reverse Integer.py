# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:21:24 2017

@author: Jinling
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return x
        #when the number is negative
        if x<0:
            return -self.reverse(-x)
        y=0
        
        while x:
            y=y*10+x%10
            x=x/10
        #return 0 when the reversed integer overflows
        return y if y <= 0x7fffffff else 0 
            