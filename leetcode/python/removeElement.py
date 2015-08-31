'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lens=len(nums)
        for i in xrange(lens-1,-1,-1):
            if nums[i]==val:
                del nums[i]
        return len(nums)
print  Solution().removeElement([1], 1)
                
        