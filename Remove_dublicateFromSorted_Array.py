'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

solve:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k

        '''


arr=list(map(int,input().split()))
k=1
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
        arr[k]=arr[i]
        k+=1
print(k,f", arr = {arr[:k]}")
