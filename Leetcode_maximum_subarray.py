#solid answer
def maxsub(nums):
        globalMax = nums[0]
        localMax = globalMax

        # iterate over the array, skipping the first one
        for i in nums[1:]:

            # decide whether its better to extend the sub-array, or start a new one from here

            # better to start a new sub-array
            if i > localMax+i:
                localMax = i

            # better to extend the array adding the current element
            else:
                localMax = localMax + i

            # check if local maxima beats global, update if so
            if localMax > globalMax:
                globalMax = localMax
        return globalMax
print(maxsub([-2,1,-3,4,-1,2,1,-5,4]))


#another answer
#answer is correct but time limit is too much.(Jaheds code)
def sub(n):
    m=n
    li=[]
    mi=[]
    sum,i,j,k,d=0,0,0,0,0
    p=[]
    if m==[]:
        return 0
    while(k<len(m)+1):
        if(d!=len(m)):
            i=0
            j=0

            while (i<len(m)-k):
                j=i+d+1
                p=m[i:j]
                for ite in p:
                    sum+=ite

                li.append(sum)
                sum=0

                mi.append(p)
                #print(p)
                i+=1

        k+=1
        d+=1

    return (max(li))
