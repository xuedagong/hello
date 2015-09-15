# -*- coding:utf-8 -*-
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 1
        if number==1:
            return 1
        if number==2:
            return 2
        #如果大于2块，最后一步 的高度可能为 1 或者为 2  转化为 n-1和n-2的情况
        return self.rectCover(number-1)+self.rectCover(number-2)
if __name__ == '__main__':
    for i in xrange(11):
        print Solution().rectCover(i)