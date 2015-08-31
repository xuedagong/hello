'''

'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum=0
        for i in xrange(len(digits)):
            sum=sum*10+digits[i]
        sum=sum+1
        lst=[]
        while sum>0:
            lst.append(sum%10)
            sum=sum/10
        lst2=[]
        lens=len(lst)
        for i in xrange( lens):
            lst2.append(lst[lens-1-i])


        return lst2

if __name__ == '__main__':
    print Solution().plusOne([1,0,1])
        