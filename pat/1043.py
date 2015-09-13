#coding=utf-8
'''
给定一个长度不超过10000的、仅由英文字母构成的字符串。请将字符重新调整顺序，按“PATestPATest....”这样的顺序输出，并忽略其它字符。
当然，六种字符的个数不一定是一样多的，若某种字符已经输出完，则余下的字符仍按PATest的顺序打印，直到所有字符都被输出。

输入格式：

输入在一行中给出一个长度不超过10000的、仅由英文字母构成的非空字符串。

输出格式：

在一行中按题目要求输出排序后的字符串。题目保证输出非空。

输入样例：
redlesPayBestPATTopTeePHPereatitAPPT
输出样例：
PATestPATestPTetPTePePee
'''
if __name__ == '__main__':
    str1=raw_input()
    P_lst=[]
    A_lst=[]
    T_lst=[]
    e_lst=[]
    s_lst=[]
    t_lst=[]
    for c in str1:
        if c=="P":
            P_lst.append(c)
        elif c=="A":
            A_lst.append(c)
        elif c=="T":
            T_lst.append(c)
        elif c=='e':
            e_lst.append(c)
        elif c=='s':
            s_lst.append(c)
        elif c=='t':
            t_lst.append(c)
    a1,a2,a3,a4,a5,a6=0,0,0,0,0,0
    out_str=""
    while a1<len(P_lst) or a2<len(A_lst) or a3<len(T_lst) or a4<len(e_lst) or a5<len(s_lst) or a6<len(t_lst):
        if a1<len(P_lst):
            out_str+=P_lst[a1]
        if a2<len(A_lst):
            out_str+=A_lst[a2]
        if a3<len(T_lst):
            out_str+=T_lst[a3]
        if a4<len(e_lst):
            out_str+=e_lst[a4]
        if a5<len(s_lst):
            out_str+=s_lst[a5]
        if a6<len(t_lst):
            out_str+=t_lst[a6]
        a1+=1
        a2+=1
        a3+=1
        a4+=1
        a5+=1
        a6+=1


    print out_str


