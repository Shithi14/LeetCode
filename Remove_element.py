'''
https://leetcode.com/problems/remove-element/
solve:

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        k=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        '''


arr=list(map(int,input().split()))
val=int(input())
k=0
for i in range(0,len(arr)):
    if arr[i]!=val:
        arr[k]=arr[i]
        k+=1

print(k,arr[:k])