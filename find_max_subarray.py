def cross(a,low,high,mid):
    lefts=-10000
    s=0
    for i in range(mid,low-1,-1):
        s=s+a[i]
        #print(s)
        if(s>lefts):
            lefts=s
            maxl=i
    rights=-10000
    s1=0
    for i in range(mid+1,high+1):
        s1=s1+a[i]
        if(s1>rights):
            rights=s1
            maxr=i
    return maxl,maxr,lefts+rights

def maxsub(a,low,high):
    if(high==low):
        return (low,high,a[low])
    else:
        mid=int((low+high)/2)
        (i,j,sum1)=maxsub(a,low,mid)
        (h,m,sum2)=maxsub(a,mid+1,high)
        (maxl,maxr,sum3)=cross(a,low,high,mid)
        if sum1>sum2 and sum1>sum3:
            return (i,j,sum1)
        elif sum2>sum1 and sum2>sum3:
            return (h,m,sum2)
        else:
            return(maxl,maxr,sum3)
                
        
a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(maxsub(a,0,len(a)-1))
