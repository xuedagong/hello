'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last_lst=[]
        for i in xrange(rowIndex+1):
            now_lst=self.get_one_list(last_lst)
            last_lst=now_lst
        return now_lst

    def get_one_list(self,last_lst):
        if len(last_lst)==0:
            return [1]
        new_lst=[]
        new_lst.append(1)
        for i in xrange(len(last_lst)-1):
            new_lst.append(last_lst[i]+last_lst[i+1])
        new_lst.append(1)
        return new_lst
if __name__ == '__main__':
    print Solution().getRow(3)
        