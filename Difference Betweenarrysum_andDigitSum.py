def numsum(nums):
       n=len(nums)
       arrsum=0
       for i in range(0,n):
            arrsum+=nums[i]
        
       digitsum=0
       for i in nums:
            while i!=0:
                r=i%10
                digitsum+=r
                i//=10
        
       result=abs(arrsum-digitsum)

       return result
        
nums=list(map(int,input().split()))
ans=numsum(nums)
print(ans)