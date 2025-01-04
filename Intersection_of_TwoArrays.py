#https://leetcode.com/problems/intersection-of-two-arrays/

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
n1=set(nums1)
n2=set(nums2)
intersection=n1&n2
print(list(intersection))