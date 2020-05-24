def happy(n):
    m=list(map(int,str(n)))
    li=[]
    sum=0

    while (True):
        sum=0
        for i in m:
            sum+=i*i
        if sum==1:
            return True
        else:
            if sum not in li:
                li.append(sum)
                m=list(map(int,str(sum)))


            else:
                return False

happy(19)     
