# -*- coding:utf-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b_lst=[]
        temp=1
        #首先计算出b0的值

        for i in xrange(1,len(A)):
            temp=temp*A[i]
        b0=temp
        b_lst.append(b0)
        j=1
        while j<len(A):
            temp=temp*
            b_lst.append()
        return b_lst

if __name__ == '__main__':
    print Solution().multiply([1,2,3])
