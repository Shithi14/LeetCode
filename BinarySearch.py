def binary(nums,t):
    l=0
    r=len(nums)

    while l<=r:
        mid=(l+r)//2
        if nums[mid]==t:
            return mid
        elif nums[mid]<t:
            l=mid+1
        else:
            r=mid-1
    
    return -1
nums=list(map(int,input().split()))
target=int(input())
ans=binary(nums,target)
print(ans)