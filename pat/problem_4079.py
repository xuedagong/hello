#coding=utf-8
'''
题目描述
令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。

输入描述:
输入在一行中给出M和N，其间以空格分隔。


输出描述:
输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。

输入例子:
5 27

输出例子:
11 13 17 19 23 29 31 37 41 43

47 53 59 61 67 71 73 79 83 89

97 101 103
'''
import math
def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True

    for i in xrange(2,int( math.sqrt(n)+1) ):
        if n%i==0:
            return False
    return True
if __name__ == '__main__':
    m,n=raw_input().split(" ")
    m=int(m)
    n=int(n)
    i=0
    temp=2
    lst=[]
    while i<n:
        if( isPrime(temp) ):#是质数
            lst.append(temp)
            i+=1
        temp+=1
    j=0
    strs=""
    for i in xrange(m-1,len(lst)):
        if j==0:
            strs=str(lst[i])
        elif j==10:
            print strs
            strs=str(lst[i])
            j=0
        else:

            strs=strs+" "+str(lst[i])
        j+=1
        # print lst[i],
    print strs
    exit(0)

