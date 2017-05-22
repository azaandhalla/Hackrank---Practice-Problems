#Given a 2D array of digits, try to find the occurrence of a given 2D pattern of digits.
import sys
import re

t = int(input().strip())
for a0 in range(t):
    temp, expression, G = ['' , '' , '']
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    for i in range(R):
        G += str(input().strip()) + '0'

    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    for i in range(r):
        expression += str(input().strip()) 
        if(i != r - 1):
             expression += '\d{' + str((C - c + 1)) +'}'

    if(re.sub(expression, "", G) != G):
        print("YES")
    else:
        print("NO")
