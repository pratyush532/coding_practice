'''
Sabarish, A doctor forms a grid where each cell represents the condition of a patient. 

The cell can take any of the three values as follows:

              1-The person is virus free

              2-The person is infected with the virus

               3-Empty cell

It takes one day for the virus to spread from one person to another. 

Every day any virus free person who is adjacent (4-directionally) to the infected person catches the disease.

Given the initial grid help the doctor to find the minimum number of days that must elapse until 

everyone has been infected. If this impossible return -1.

Example:-

Suppose the input grid is 2 1 1 

                                            1 1 3

                                            3 1 1

After day 1 the grid will be    2 2 1

                                                  2 1 3

                                                  3 1 1

After day 2 the grid  will be  2 2 2

                                                 2 2 3

                                                 3 1 1

 

After day 3 the grid will be 2 2 2

                                               2 2 3

                                               3 2 1

After day 4 the grid will be 2 2 2

                                               2 2 3

                                               3 2 2

So, the minimum number of days is 4

Input format:-

Numbers of row in the grid

Numbers of column in the grid

Contents of the grid(next row*column lines)

Output format:-

Minimum number of days required'''

def check(l): #if all infected = True, else False
    flag = True
    for i in l:
        for j in i:
            if j==1:
                flag = False
                break
    return flag

l = [[2,1,1],[1,1,3],[3,1,1]]
r = 3
c = 3
a= 1
while (True):
    coll = []

    for i in range(0,r):
        for j in range(0,c):
            if l[i][j]==2:
                coll = coll + [[i,j]]


    for i in range(0,r):
        for j in range(0,c):
            if [i,j] in coll:
                #rows updation
                if j+1>=0 and j+1<=c-1 and l[i][j+1]==1:
                    l[i][j+1]= 2
                if j-1>=0 and j-1<=c-1 and l[i][j-1]==1:
                    l[i][j-1]= 2
                #colunmns updation
                if i+1>=0 and i+1<=r-1 and l[i+1][j]==1:
                    l[i+1][j]=2
                if i-1>=0 and i-1<=r-1 and l[i-1][j]==1:
                    l[i-1][j]=2
    print("DAY "+str(a))
    for i in l:
        print(i)
    if check(l)==False:
        print("Not all infected")
        a = a+1
    else:
        print("Min no of days = ", a)
        break