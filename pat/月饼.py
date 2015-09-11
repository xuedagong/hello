#coding=utf-8
'''
题目描述
月饼是中国人在中秋佳节时吃的一种传统食品，不同地区有许多不同风味的月饼。现给定所有种类月饼的库存量、总售价、以及市场的最大需

求量，请你计算可以获得的最大收益是多少。



注意：销售时允许取出一部分库存。样例给出的情形是这样的：假如我们有3种月饼，其库存量分别为18、15、10万吨，总售价分别为75、

72、45亿元。如果市场的最大需求量只有20万吨，那么我们最大收益策略应该是卖出全部15万吨第2种月饼、以及5万吨第3种月饼，获得

 72 + 45/2 = 94.5（亿元）。

输入描述:
每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N表示月饼的种类数、以及不超过500（以万吨为单位）的正整数

D表示市场最大需求量。随后一行给出N个正数表示每种月饼的库存量（以万吨为单位）；最后一行给出N个正数表示每种月饼的总售价（以亿

元为单位）。数字间以空格分隔。


输出描述:
对每组测试用例，在一行中输出最大收益，以亿元为单位并精确到小数点后2位。

输入例子:
3 20
18 15 10
75 72 45

输出例子:
94.50
'''

# print 72*1.0/15
# print 45*1.0/10
# print 75*1.0/18

n,need=raw_input().split(" ")
n=int(n)  #多少种月饼
need=int(need)
kucun=raw_input().split(" ")
money_list=raw_input().split(" ")
for i in xrange(n):
    kucun[i]=int(kucun[i])
    money_list[i]=int(money_list[i])

money_p=[]
for i in xrange(n):
    if kucun[i]>0:
        money_p.append( money_list[i]*1.0/kucun[i])
    else:
        money_p.append( 0.0)

dicts={}
for i in xrange(n):
    dicts[i]=money_p[i]

money_p_cp=money_p[:]
money_p.sort(reverse=True)
sort_index=[]
for i in xrange(n):
    for (k,v) in dicts.items():
        if v==money_p[i]:
            sort_index.append(k)
            del dicts[k]
            break
# print sort_index
sum=0.0
total=need
for index_i in sort_index:
    if total>kucun[index_i]:
        total=total-kucun[index_i]
        sum+= kucun[index_i]*money_p_cp[index_i]
    else:
        sum+= total*money_p_cp[index_i]
        break
print '%.2f'%sum
exit(0)


