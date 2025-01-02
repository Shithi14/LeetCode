'''
https://leetcode.com/problems/search-insert-position/
solve:

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        #the value is not found then insert
      
        return left

        '''





arr=list(map(int,input().split()))
t=int(input())
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==t:
        print(mid)
    elif arr[mid]<t:
        l=mid+1
    else:
        r=mid-1

else:
    print(l)

