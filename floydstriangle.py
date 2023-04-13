#floyd's triangle
r=int(input("enter no. of rows"))
num=1
print("Floyd's triangle")
for i in range(1,r+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print("")