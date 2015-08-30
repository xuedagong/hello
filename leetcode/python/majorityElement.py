#coding=utf-8
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list={}
        lens=len(nums)
        half_num=lens/2
        for item in nums:
            if item in new_list:
                new_list[ item ]+=1
                if new_list[item]>half_num:
                    return item
            else:
                new_list[ item ]=1
                if new_list[item]>half_num:
                    return item


        