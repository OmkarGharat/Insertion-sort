a = [7,5,3,4,8]
print("List before sorted : ",a)
 
for i in range(1,len(a)):
    for j in range(0,i):
        if a[i]<a[j]:
            temp = a.pop(i)
            a.insert(j,temp)
            break

print("List after sorted  : ",a)
