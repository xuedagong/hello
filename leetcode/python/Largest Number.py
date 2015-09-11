#coding=utf-8
'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution(object):
    #主要的问题 3 30  这种排序
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_lst=[]
        for one_num in nums:
            str_lst.append(str(one_num))
        str_lst.sort( cmp=lambda x, y: cmp(y + x, x + y),  reverse=False)
        strs=''.join(str_lst)
        return strs.lstrip('0') or '0'
print Solution().largestNumber([0,0])
            