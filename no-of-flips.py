
def generateGrayarr(n):
    if (n <= 0):
        return
    arr = list()
    arr.append("0")
    arr.append("1")
    i = 2
    j = 0
    while(True):
 
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
        for j in range(i):
            arr[j] = "0" + arr[j]
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]
        i = i << 1
    # for i in range(len(arr)):
    #     print(arr[i])
    return arr
n = 5

s="11??0"

c = 0
for i in range(0,len(s)):
    if s[i]=="?":
        c = c+ 1
#print(c)

arr = generateGrayarr(c)
#print(arr)

minlist = []

for i in range(0,len(arr)):
    l = s
    l = l.replace("??",arr[i])
    print(l,l.count('01')+l.count('10'))
    minlist+=[l.count('01')+l.count('10')]
print(min(minlist))