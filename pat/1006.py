#coding=utf-8
'''
让我们用字母B来表示“百”、字母S表示“十”，用“12...n”来表示个位数字n（<10），
换个格式来输出任一个不超过3位的正整数。例如234应该被输出为BBSSS1234，因为它有2个“百”、3个“十”、以及个位的4。

输入格式：每个测试输入包含1个测试用例，给出正整数n（<1000）。

输出格式：每个测试用例的输出占一行，用规定的格式输出n。

输入样例1：
234
输出样例1：
BBSSS1234
输入样例2：
23
输出样例2：
SS123
'''
#coding=utf-8
#最大数字为999
def get_geshu_str(n):
    strs=''
    for i in xrange(n):
        strs=strs+str(i+1)
    return strs
if __name__=="__main__":
#     print "S"*3
#     exit();
    n=raw_input()
    n=int(n)
    lst=[0,0,0] #分别表示 个，十 ，百
    index_i=0
    while n>0:
        lst[index_i]=n%10
        index_i+=1
        n=n/10
    print "B"*lst[2]+"S"*lst[1]+get_geshu_str(lst[0])
        
    