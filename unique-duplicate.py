
l = [3,4,5,5,7,1,2,3,45,6]

u,d =[],[]

for i in range(0,len(l)):
    if l[i] not in d :      #for duplicate elements
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                d = d + [l[i]]
    if (len([ l[k]for k in range(0,len(l)) if l[k]==l[i]])==1):  #for unique elements
        u =u + [l[i]]
        
print("Duplicate elements = ",d)
print("Unique elements = ",u)