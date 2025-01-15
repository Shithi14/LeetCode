#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
nums=list(map(int,input().split()))
maxi=sorted(nums)
M1=maxi[-1]
M2=maxi[-2]
sum=(M1-1)*(M1-1)
print(sum)

