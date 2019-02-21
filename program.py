l=[]
s=int(input("enter list size"))
for i in range(s):
    x=int(input("enter list items: ")    )
    l.append(x)
print("the list is",l)  
l.sort()
f=int(input("enter a number to search for: "))
c=0
for i in l:
    if f==i:
        c=1
        print("entered number",f,"is present at position",l.index(f)+1)
        break

if c==0:
    print("entered number is not present in list")
