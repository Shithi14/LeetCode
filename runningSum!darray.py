#https://leetcode.com/problems/running-sum-of-1d-array/

def arrsum(nums):
    sum=0
    arr=[]
    for i in range(0,len(nums)):
        sum+=nums[i]
        arr.append(sum)

    return arr


nums=[1,2,3,4]
ans=arrsum(nums)
print(ans)