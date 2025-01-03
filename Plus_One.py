'''
https://leetcode.com/problems/plus-one/
solve:



'''
nums = list(map(int, input().split()))
l = len(nums)
for i in range(l - 1, -1, -1):
    if nums[i] < 9:
        nums[i] += 1
        break
    else:
        nums[i] = 0
        
else:
    nums = [1] + nums

print(nums)