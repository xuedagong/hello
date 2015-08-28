#coding=utf-8
'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_cnt=1  #非质数的数量  1是质数
        is_prime_list=[True] * n


        for i in xrange(2,n):
            if is_prime_list[i]==False:
                continue
            else:
                j=2
                while i*j<n:
                    is_prime_list[ i*j  ]=False
                    j=j+1
        cnt=0
        for i in xrange(2,n):
            if is_prime_list[i]:
                cnt=cnt+1
        return cnt


print Solution().countPrimes(1500000) #  2,3,5,7 =>4

        