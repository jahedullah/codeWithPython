def re(x):

        if (x<0):
            sign=-1
        else:
            sign =1
        x*=sign

        x=str(x)
        li=list(x)
        li.reverse()
        x=''.join(li)
        x=int(x)*sign
        if(x>2**31 or x<-(2**31)-1):
            return 0
        else:
            return x


print(re(1534236469))
