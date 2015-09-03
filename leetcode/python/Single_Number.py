'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts ={}
        for item in nums:
            if item not in dicts:
                dicts[item]=1
            else:
                dicts[item]+=1
        for key in dicts:
            if dicts[key]==1:
                return key

if __name__ == '__main__':
    print Solution().singleNumber([15,2,3,3,2,15,99])
