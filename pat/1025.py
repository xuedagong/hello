#coding=utf-8
'''
给定一个常数K以及一个单链表L，请编写程序将L中每K个结点反转。例如：给定L为1→2→3→4→5→6，K为3，则输出应该为3→2→1→6→5→4；如果K为4，则输出应该为4→3→2→1→5→6，即最后不到K个元素不反转。

输入格式：

每个输入包含1个测试用例。每个测试用例第1行给出第1个结点的地址、结点总个数正整数N(<= 105)、以及正整数K(<=N)，即要求反转的子链结点的个数。结点的地址是5位非负整数，NULL地址用-1表示。

接下来有N行，每行格式为：

Address Data Next

其中Address是结点地址，Data是该结点保存的整数数据，Next是下一结点的地址。

输出格式：

对每个测试用例，顺序输出反转后的链表，其上每个结点占一行，格式与输入相同。

输入样例：
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218
输出样例：
00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1
'''
if __name__=='__main__':
    head,n,move=raw_input().split(" ")
    n=int(n)
    move=int(move)
    lst=[]
    for i in xrange(n):
        a,b,c=raw_input().split(" ")
        lst.append((a,b,c))
    new_lst=[]
    index_i=0
    while index_i<n:
        for item in lst:
            if head==item[0]:
                new_lst.append(item)
                head=item[2]
                index_i+=1
    for i in xrange(move-1,-1,-1):
        if i==0:
            next_index=new_lst[move-1][2]
        else:
            next_index=new_lst[(i-1)][0]
        print new_lst[i][0],new_lst[i][1],next_index
        
    for i in xrange(move,n):
        print new_lst[i][0],new_lst[i][1],new_lst[i][2] 
        
        
    