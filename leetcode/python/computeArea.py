#coding=utf8
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        one_x=[A,C]
        
        one_y=[B,D]
        one_x.sort()
        one_y.sort()
        
        two_x=[E,G]
        two_y=[F,H]
        two_x.sort()
        two_y.sort()
        
        x_list=[ A,C,E,G ]
        x_list.sort();
        
        y_list=[B,D,F,H ]
        y_list.sort();
        common_x=( one_x[1]-one_x[0] ) + ( two_x[1]-two_x[0] ) -  abs(x_list[3]-x_list[0] )
        common_y=( one_y[1]-one_y[0] ) + ( two_y[1]-two_y[0] ) -  abs(y_list[3]-y_list[0] )
        
        if common_x <0 or common_y<0:   #重复的面积
            common= 0
        else:
            common= common_x*common_y    #重复的面积
        one_area= ( one_x[1]-one_x[0] )* ( one_y[1]-one_y[0] )
        two_area= ( two_x[1]-two_x[0] )* ( two_y[1]-two_y[0] )
        return two_area+one_area-common
print Solution().computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
        
        
        