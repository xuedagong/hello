# -*- coding:utf-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b_lst=[]
        n=len(A)
        temp=1
        #首先计算出b0的值
        b_lst.append(1)
        for i in xrange(0,len(A)-1):
            temp=temp*A[i]
            b_lst.append(temp)
        print b_lst
        #这个时候的 bi = a0*a1..*ai-1


        for i in xrange(1,len(A)):
            for j in xrange(i):
                b_lst[j]*=A[i]
        #这一步把bi得后半部分补回来 bi=bi* a(i+1)*a(i+2)*.....*a(n-1)
        return b_lst

if __name__ == '__main__':
    print Solution().multiply([1,2,3])
    print Solution().multiply([1,2,3,4,5])
    print Solution().multiply([1])
