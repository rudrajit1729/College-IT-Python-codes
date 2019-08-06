n=int(input('Enter the number:'))
flag=1
for i in range (2,n//2):
    if n%i==0:
        print("Composite Number")
        flag=0
if flag==1:
    print("Prime Number")
