#coding=utf-8
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lst=[]
        last_lst=[]
        for i in xrange(numRows):
            now_lst=self.get_one_list(last_lst)
            lst.append(now_lst)
            last_lst=now_lst
        return lst

    #根据上一个队列来生成新的队列
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
    print Solution().generate(0)


