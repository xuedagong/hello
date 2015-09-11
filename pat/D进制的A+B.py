#coding=utf-8
'''
<<<<<<< HEAD
题目描述
输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。

输入描述:
输入在一行中依次给出3个整数A、B和D。


输出描述:
输出A+B的D进制数。

输入例子:
123 456 8

输出例子:
1103
'''
if __name__ == '__main__':
    a,b,d=raw_input().split(" ")
    int1=int(a)
    int2=int(b)
    d=int(d)
    sum=int1+int2
    strs=""
    while sum>0:
        strs=str(sum%d)+strs
        sum=sum/d
    print strs
=======
输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。

输入格式：

输入在一行中依次给出3个整数A、B和D。

输出格式：

输出A+B的D进制数。

输入样例：
123 456 8
输出样例：
1103
'''
a,b,d=raw_input().split(" ")
sum=int(a)+int(b)
d=int(d)
famart_str=''
while sum>0:
    famart_str=str(sum %d)+famart_str
    sum=sum/d
if famart_str=='':
    famart_str=0
famart_int=int(famart_str)
   
print famart_int
>>>>>>> 7bf0a1d96001105555bb3376f9c18bf9484f8556
