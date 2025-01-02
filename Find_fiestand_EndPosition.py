arr=list(map(int,input().split()))
target=int(input())
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid-1,mid+1)
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
print([-1,-1])