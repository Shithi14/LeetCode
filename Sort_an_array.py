#https://leetcode.com/problems/sort-an-array/
def mergearr(arr,l,mid,r):
    

    n1=mid-l+1
    n2=r-mid

    arr1=[0]*n1
    arr2=[0]*n2

    for i in range(n1):
        arr1[i]=arr[i+l]

    for j in range(n2):
        arr2[j]=arr[mid+1+j]
    
    i=j=0
    k=l

    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            arr[k]=arr1[i]
            i+=1
            k+=1
    

        else:
            arr[k]=arr2[j]
            j+=1
            k+=1
    

    while i<n1:
        arr[k]=arr1[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k]=arr2[j]
        j+=1
        k+=1


def merge(arr,l,r):
    mid=l+(r-l)//2

    if l==r:
        return
    else:
        merge(arr,l,mid)
        merge(arr,mid+1,r)
        mergearr(arr,l,mid,r)
    
    return arr
  



nums=list(map(int,input().split()))
ans=merge(nums,0,len(nums)-1)
print(ans)