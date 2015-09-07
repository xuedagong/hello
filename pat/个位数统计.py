if __name__ == '__main__':
    n=raw_input()
    dicts={}
    # for i in xrange(10):
    #     k=str(i)
    #     dicts[k]=0
    for item in n:
        if item not in dicts:
            dicts[item]=1
        else:
            dicts[item]+=1
    lst=dicts.keys()
    lst.sort()
    for k in lst:
        print k+':'+str(dicts[k])
