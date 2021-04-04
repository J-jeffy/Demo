s=input()
b,l,n=0,0,0 
for i in s:
    if i.islower():
        l+=1
    elif i.isupper():
        b+=1
    elif i.isdigit():
        n+=1
print(b,end='\n')
print(l,end='\n')
print(n)
