n=int(input("enter the n value"))
r=int(input("enter the r value"))
c=n-r
a=1
for i in range(1,n+1):
    a=a*i
b=1
for j in range(1,r+1):
    b=b*j
d=1
for k in range(1,c+1):
    d=d*k
e=int(a/(b*d))
print (e)
