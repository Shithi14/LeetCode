'''
https://leetcode.com/problems/find-target-indices-after-sorting-array/

solve:
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr=sorted(nums)
        result=[]
        for i in range(0,len(arr)):
            if arr[i]==target:
               result.append(i)
        return result
        '''

arr=list(map(int,input().split()))
target=int(input())
sortarray=sorted(arr)
result=[]
for i in range(0,len(sortarray)):
    if sortarray[i]==target:
        result.append(i)
print(result)