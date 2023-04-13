#checks if the second string is substring of the first string
k=input("enter first string")
s=input("Enter second string")
m=len(s)
p=0
for i in range(len(k)):
    if s[0]==k[i]:
        p=p+1
        continue
    if p>=1:
        for j in range(p,m):
            if s[j]==k[i]:
                p+=1
                break
if p==m:
    print(f"{s} is a sub string of {k}")
else:
    print(f"{s} is a not sub string of {k}")