li = [7,1,5,3,6,4]
minval=li[0]
ans = 0
for i in range(1,len(li)):
    ans = max(ans,(li[i]-minval))
    minval=min(minval,li[i])
print(ans)


#brute force method
li=[7,1,5,3,6,4]
n = len(li)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if li[i]<li[j]:
            temp= li[j]-li[i]
            ans = max(temp,ans)
print(ans)
