#coding=utf-8
'''
题目描述
正整数A的“DA（为1位整数）部分”定义为由A中所有DA组成的新整数PA。例如：给定A = 3862767，DA = 6，则A的“6部分”PA是66，因为A中有2个6。



现给定A、DA、B、DB，请编写程序计算PA + PB。

输入描述:
输入在一行中依次给出A、DA、B、DB，中间以空格分隔，其中0 < A, B < 1010。


输出描述:
在一行中输出PA + PB的值。

输入例子:
3862767 6 13530293 3

输出例子:
399
'''
def get_s1_common(s1,s2):
    com_s=''
    for item in s1:
        if item==s2:
            com_s+=item
    if com_s=='':
        com_s='0'
    return com_s
if __name__ == '__main__':
    s1,s2,s3,s4=raw_input().split(" ")
    com1=get_s1_common(s1,s2)
    com2=get_s1_common(s3,s4)
    sum=int(com1)+int(com2)
    print sum
    exit(0)
