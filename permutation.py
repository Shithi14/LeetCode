#https://leetcode.com/problems/permutations/

def permutation(s,l,r,result):
    if l==r:
        result.append(list(s))
    else:
        for i in range(l,r+1):
            s[l],s[i]=s[i],s[l]
            permutation(s,l+1,r,result)
            s[l],s[i]=s[i],s[l]



nums=list(map(int,input().split()))
n=len(nums)
result=[]
permutation(nums,0,n-1,result)
print(result)
