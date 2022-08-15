

def bubblesort(l) :
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l



l = [2,3,1,4,2,6,8,4,7,9,33]
print(bubblesort(l))
