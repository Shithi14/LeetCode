'''
https://leetcode.com/problems/missing-number/


'''

nums=list(map(int,input().split()))
n=len(nums)
totalsum=(n*(n+1)//2)
Sum=0
for i in range (0,len(nums)):
    Sum+=nums[i]

print(totalsum-Sum)