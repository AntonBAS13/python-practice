n = int(input())
q = 0
q1 = 0
q2 = 0
mark1 = ''
mark2 = ''
mark3 = ''

for i in range(n):
    mark = input()
    if mark == mark1:
        q += 1
    elif mark == mark2:
        q1 += 1
    elif mark == mark3:
        q2 += 1
    else:
        if mark1 == '':
            mark1 = mark
            q = 1
        elif mark2 == '':
            mark2 = mark
            q1 = 1
        else:
            mark3 = mark
            q2 = 1
            
if q > 0:
    print((mark1, q))
if q1 > 0:
    print((mark2, q1))
if q2 > 0:
    print((mark3, q2))
                