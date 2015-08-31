#coding=utf-8
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #
        i,j=0,0
        while i<m and j<n:
            # print nums1[i]
            if nums1[0]>=nums2[j]:# num1中放大数，所以必须nums[0] 大于所有的nums2
                j+=1
            else:# 出现了nums2[j]比nums1中大的数字 ,需要和 nums[0]进行交换
                k=0
                change_num=nums2[j]
                nums2[j]=nums1[0]
                while k<m and nums1[k]<change_num:
                    nums1[k]=nums1[k+1]
                    k+=1

                k=k-1
                nums1[k]=change_num
                # j+=1


        k=0
        while k<m:
            nums1[m-1-k+n]=nums1[m-1-k]
            k+=1
        k=0
        while k<n:

            nums1[k]=nums2[k]
            k+=1
        print nums1

if __name__ == '__main__':
    a=[3,5]
    Solution().merge([1,0], 1, [2], 1)
    Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    Solution().merge([1,2,4,5,6,0], 5, [3], 1)
    # print a
