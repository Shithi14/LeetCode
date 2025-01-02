'''#https://leetcode.com/problem-list/array/

Answer:

arr=list(map(int,input().split()))
target=int(input())
found=False
for i in  range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([i,j])
            found=True
            break
if not found:
    print([])
   

'''

arr=list(map(int,input().split()))
target=int(input())
found=False
for i in  range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([i,j])
            found=True
            break
    if found:
        break
if not found:
    print([])
   

