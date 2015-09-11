#coding=utf-8
'''
根据维基百科的定义：

插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置。如此迭代直到全部元素有序。

归并排序进行如下迭代操作：首先将原始序列看成N个只包含1个元素的有序子序列，然后每次迭代归并两个相邻的有序子序列，直到最后只剩下1个有序的序列。

现给定原始序列和由某排序算法产生的中间序列，请你判断该算法究竟是哪种排序算法？

输入格式：

输入在第一行给出正整数N (<=100)；随后一行给出原始序列的N个整数；最后一行给出由某排序算法产生的中间序列。这里假设排序的目标序列是升序。数字间以空格分隔。

输出格式：

首先在第1行中输出“Insertion Sort”表示插入排序、或“Merge Sort”表示归并排序；然后在第2行中输出用该排序算法再迭代一轮的结果序列。题目保证每组测试的结果是唯一的。数字间以空格分隔，且行末不得有多余空格。
输入样例1：
10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0
输出样例1：
Insertion Sort
1 2 3 5 7 8 9 4 6 0


输入样例2：
10
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6
输出样例2：
Merge Sort
1 2 3 8 4 5 7 9 0 6

'''
#lst需要排序的lst,
#ord_lst产生的中间序列
def InsertionSort(lst):
    n=len(lst)
    step_lst=[]
    for i in xrange(1,n):
        find_index=False
        for j in xrange(i):#对于第i个元素，在i-1列表中 找到其正确的位置
            if lst[j]>lst[i]:
                find_index=True
                break
        if find_index==False:#表示i就在其正确的位置 不需要做任何改变
            pass
        else:#正确的位置在j上面
            temp=lst[i]
            for k in xrange(i,j,-1):# 把[j,i-1]的元素，右边移动一位
                lst[k]=lst[k-1]
            lst[j]=temp
        ss= " ".join(lst)
        print ss

        step_lst.append(ss)
    print step_lst
    return step_lst

def MergeSort(lst):


if __name__ == '__main__':
    n=raw_input()
    # lst=map(int,raw_input().split(" ") )
    lst=raw_input().split(" ")
    lst1= InsertionSort(lst)
    n1=len(lst1)
    print lst1[ (n1/2)-1 ]








