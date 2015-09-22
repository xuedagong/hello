#coding=utf-8
'''
令Pi表示第i个素数。现任给两个正整数M <= N <= 104，请输出PM到PN的所有素数。

输入格式：

输入在一行中给出M和N，其间以空格分隔。

输出格式：

输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。

输入样例：
5 27
输出样例：
11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
'''
#coding=utf-8
import math
if __name__=="__main__":
    m,n=map(int,raw_input().split(" ") )
    max_n=100000
    lst=[]
    
    for i in xrange(max_n+1):
        lst.append(True)#是质数 
    lst[1]=False
    lst[2]=True
    for i in xrange(2,int(math.sqrt(max_n))+1):
        if lst[i] ==True:#是质数
            k=2
            while i*k<=max_n:
                lst[ i*k  ]=False
                k+=1
#     for i in xrange(1,n+1):
#         print i,lst[i]
    index_i=0
    zhishu_lst=[]
    for i in xrange(2,max_n+1):
        if lst[i]==True : #是质数
            index_i+=1
            zhishu_lst.append(i)
            if index_i==n:
                break
    print_index=0
    for k in xrange(m-1,n):
        
        print_index+=1
        if print_index==10:
            print_index=0
            print zhishu_lst[k]
        else:
            print zhishu_lst[k],
