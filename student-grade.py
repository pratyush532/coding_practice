'''
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade  and the next multiple of 5  is less than , round  up to the next multiple of 5 .
If the value of grade is less than 3 , no rounding occurs as the result will still be a failing grade.'''

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    x =[]
    for i in grades:
        if i%10<=5:
            x+=[5-(i%10)]
        elif i%10>5:
            x+=[10-(i%10)]
    #print(x)
    res = []
    for i in range(0,len(x)):
        if x[i]<3 and grades[i]>=38:
            res+=[grades[i]+x[i]]
        elif x[i]>=3:
            res+=[grades[i]]
        elif grades[i]<38:
            res+=[grades[i]]
    return res

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    for i in result :
        print(i)

'''
4
73
67
38
33
[2, 3, 2, 2]
[75, 67, 40, 33]
'''