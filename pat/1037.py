#coding=utf-8
'''
如果你是哈利·波特迷，你会知道魔法世界有它自己的货币系统 —— 就如海格告诉哈利的：
“十七个银西可(Sickle)兑一个加隆(Galleon)，二十九个纳特(Knut)兑一个西可，很容易。”
现在，给定哈利应付的价钱P和他实付的钱A，你的任务是写一个程序来计算他应该被找的零钱。

输入格式：

输入在1行中分别给出P和A，格式为“Galleon.Sickle.Knut”，
其间用1个空格分隔。这里Galleon是[0, 107]区间内的整数，Sickle是[0, 17)区间内的整数，Knut是[0, 29)区间内的整数。

输出格式：

在一行中用与输入同样的格式输出哈利应该被找的零钱。如果他没带够钱，那么输出的应该是负数。

输入样例1：
10.16.27 14.1.28
输出样例1：
3.2.1
输入样例2：
14.1.28 10.16.27
输出样例2：
-3.2.1
'''

'''
Sickle Galleon 17:1
Knut   Sickle  29:1

'''
def get_res_str(n):
    lst=[]
    temp=n
    n=abs(n)
    lst.append(n%29)
    n=n/29
    lst.append(n%17)
    lst.append(n/17)
    s=str(lst[2])+'.'+str(lst[1])+'.'+str(lst[0])
    if temp<0:
        s="-"+s
    return s
if __name__=="__main__":
    P,A=raw_input().split(" ")
    plst=P.split(".")
    alst=A.split(".")
    sum_p=int(plst[0])*17*29+int(plst[1])*29+int(plst[2])
    sum_a=int(alst[0])*17*29+int(alst[1])*29+int(alst[2])
    res=sum_a-sum_p
    print get_res_str(res)