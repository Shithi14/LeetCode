'''
https://leetcode.com/problems/contains-duplicate/

solve:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniquenum=set(nums)
        if len(nums)==len(uniquenum):
            return False
        return True

        

'''

arr = list(map(int, input().split()))

uniquenum = set()

for i in arr:
    if i in uniquenum:
        print("true")
        break
    uniquenum.add(i)
else:
    print("false")
