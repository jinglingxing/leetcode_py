# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:41:43 2017

@author: Jinling
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=temp=ListNode(0)
        carry=0
        while(l1 or l2):
            temp1=l1.val if l1 else 0
            temp2=l2.val if l2 else 0
            val=temp1+temp2+carry
            carry= val/10
            val=val%10
            temp.next= ListNode(val)
            temp= temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            temp.next= ListNode(carry)
            temp=temp.next
        return head.next
        