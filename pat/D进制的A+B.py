#coding=utf-8
'''
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