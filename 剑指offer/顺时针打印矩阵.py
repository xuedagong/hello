#coding=utf-8
'''
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
1  2   3  4
5  6   7  8
9  10  11 12
13 14  15 16
'''
#coding=utf-8
import math
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        start_i=0
        end_i=len(matrix)
        end_j=len(matrix[0])
        print_lst=[]
        while start_i<end_i and start_i<end_j:
            i=start_i
            j=start_i
            
            #1
            while j<end_j:
                print_lst.append(matrix[i][j])
                j+=1
                
            i+=1
            j-=1
            #2
            while i<end_i:
                
                print_lst.append(matrix[i][j])
                i+=1
            
            j-=1
            i-=1
            
            #3
            while j>=start_i and i>start_i:
                print_lst.append(matrix[i][j])
                j-=1
            
            i-=1 
            j+=1 
            #4
            while i>start_i and j<end_j-1 :
                print_lst.append(matrix[i][j])
                i-=1  
                
            start_i+=1
            end_i-=1
            end_j-=1
        return print_lst
        # write code here
        
if __name__=='__main__':
    
    print Solution().printMatrix([[1,2,3,4,5]])
    print Solution().printMatrix([[1],[2],[4],[5]])
    print Solution().printMatrix([[1]])
    print Solution().printMatrix([[]])
    print Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])    
            
        