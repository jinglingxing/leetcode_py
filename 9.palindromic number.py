# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:35:51 2017

@author: Jinling
"""
#  palindromic letter checking回文检测
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==0:
            return True
        temp=x
        y=0
        while x:
    
            y = y*10 + x%10;
            x=x/10
        if temp==y:
            return True
        else:
            return False
                
            
        
        