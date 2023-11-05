l=int(input("Enter value of L:"))
r=int(input("Enter value of R:"))
if l<r:
    li = []
    for i in range(l,r+1):
        temp = str(i)
        ln=len(temp)
        if temp[ln-1]=='2':
            li.append(temp)
        if temp[ln-1]=='3':
            li.append(temp)
        if temp[ln-1]=='9':
            li.append(temp)
else:
    print("Enter value of L which is smaller than R!")
print(len(li))