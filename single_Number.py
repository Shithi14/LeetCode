nums=list(map(int,input().split()))
result=0
for i in  range(0,len(nums)):
    result^=nums[i]
print(result)

