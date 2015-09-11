#coding=utf-8
'''
## 1007. 素数对猜想 (20)
让我们定义 dn 为：dn = pn+1 - pn，其中 pi 是第i个素数。显然有 d1=1 且对于n>1有 dn 是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。

现给定任意正整数N (< 105)，请计算不超过N的满足猜想的素数对的个数。

输入格式：每个测试输入包含1个测试用例，给出正整数N。

输出格式：每个测试用例的输出占一行，不超过N的满足猜想的素数对的个数。

输入样例：
20
输出样例：
4
'''
#coding=utf-8
import math
if __name__=="__main__":
    n=raw_input()
    n=int(n)
    lst=[]
    if n<2:
        print 0
        exit(0)
    for i in xrange(n+1):
        lst.append(True)#是质数 
    lst[1]=False
    lst[2]=True
    for i in xrange(2,int(math.sqrt(n))+1):
        if lst[i] ==True:#是质数
            k=2
            while i*k<=n:
                lst[ i*k  ]=False
                k+=1
#     for i in xrange(1,n+1):
#         print i,lst[i]
    dui_num=0
    for i in xrange(1,n+1-2):
        if lst[i]==True and lst[i+2]==True:
            dui_num+=1
    print dui_num
            
        