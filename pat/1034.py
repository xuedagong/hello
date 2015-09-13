#coding=utf-8
'''
本题要求编写程序，计算2个有理数的和、差、积、商。

输入格式：

输入在一行中按照“a1/b1 a2/b2”的格式给出两个分数形式的有理数，其中分子和分母全是整型范围内的整数，负号只可能出现在分子前，分母不为0。

输出格式：

分别在4行中按照“有理数1 运算符 有理数2 = 结果”的格式顺序输出2个有理数的和、差、积、商。注意输出的每个有理数必须是该有理数的最简形式“k a/b”，
其中k是整数部分，a/b是最简分数部分；若为负数，则须加括号；若除法分母为0，则输出“Inf”。题目保证正确的输出中没有超过整型范围的整数。

输入样例1：
2/3 -4/2
输出样例1：
2/3 + (-2) = (-1 1/3)
2/3 - (-2) = 2 2/3
2/3 * (-2) = (-1 1/3)
2/3 / (-2) = (-1/3)
输入样例2：
5/3 0/6
输出样例2：
1 2/3 + 0 = 1 2/3
1 2/3 - 0 = 1 2/3
1 2/3 * 0 = 0
1 2/3 / 0 = Inf
'''
#coding=utf-8
#求x,y的最大公约数
def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    hcfs=1
    for i in range(1,smaller+1):
        if  x%i==0 and y%i==0:
            hcfs=i
    return hcfs
#把一个输入的有理数转为最简单的类型
def get_good(lst):
    a,b=lst[0],lst[1];
    if b==0:
        return "Inf"
    if a==0:
        return "0"

    a_abs=abs(a)
    hcfs=hcf(a_abs,b)
    a_abs,b=a_abs/hcfs,b/hcfs
    str_lst=[]
    zhengshu=a_abs/b
    yushu = a_abs%b
    if zhengshu>0:
        str_lst.append(str(zhengshu))

    res= str(zhengshu)
    if yushu>0:
        str_lst.append( str(yushu)+"/"+str(b) )
    res=" ".join(str_lst)

    if a<0:  #为负数，必须加上 （）
        return "(-"+res+")"
    else:
        return res

#根据str1 ，str2返回其计算结果
def get_add(lst1,lst2):
    new_lst=[]
    new_lst.append( lst1[0]*lst2[1]+lst1[1]*lst2[0])
    new_lst.append(  lst1[1]*lst2[1] )
    return new_lst

def get_minus(lst1,lst2):
    new_lst=[]
    new_lst.append( lst1[0]*lst2[1]-lst1[1]*lst2[0] )
    new_lst.append(  lst1[1]*lst2[1] )
    return new_lst

def get_mul(lst1,lst2):
    new_lst=[]
    new_lst.append(  lst1[0]*lst2[0]  )
    new_lst.append(  lst1[1]*lst2[1]  )
    return new_lst

def get_div(lst1,lst2):
    new_lst=[]
    if lst1[0]*lst2[0]<0:
        flag=-1
    else:
        flag=1
    new_lst.append(  flag* abs( lst1[0]*lst2[1] )  )
    new_lst.append(  abs( lst1[1]*lst2[0] ) )
    return new_lst









if __name__ == '__main__':
    # print get_good([4,4])
    # exit(0)
    str1,str2=raw_input().split(" ")
    lst1=map(int,str1.split('/'))
    lst2=map(int,str2.split("/"))


    print get_good(lst1),"+",get_good(lst2),"=",get_good( get_add(lst1,lst2) )
    print get_good(lst1),"-",get_good(lst2),"=",get_good( get_minus(lst1,lst2) )
    print get_good(lst1),"*",get_good(lst2),"=",get_good( get_mul(lst1,lst2) )
    print get_good(lst1),"/",get_good(lst2),"=",get_good( get_div(lst1,lst2) )