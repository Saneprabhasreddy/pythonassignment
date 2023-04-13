#palidrome
k=input("Enter a string ")
s=""
for i in k:
    s=i+s
print(s)
if s==k:
    print("given string is a palindrome")
else:
    print("given strin is not a palindrome")