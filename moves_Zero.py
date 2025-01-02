'''
https://leetcode.com/problems/move-zeroes/
solve:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
                
        for i in range(k,len(nums)):
            nums[i]=0

        return nums
        '''


arr=list(map(int,input().split()))
k=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        arr[k]=arr[i]
        k+=1
for i in range (k,len(arr)):
    arr[i]=0
print(len(arr), f"num = {arr}")
