string=input()
s=''
for i in string:
    if i not in s:
        s=s+i
print(s)
