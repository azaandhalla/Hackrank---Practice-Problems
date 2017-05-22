#A queen is standing on an n X n chessboard. The chessboard's rows are numbered from 1 to n, going from bottom to top; its columns are numbered from 1 to n, going from left to right. Each square on the board is denoted by a tuple, (r,c) , describing the row, r, and column, c, where the square is located. The queen is standing at position (rq,cq) and, in a single move, she can attack any square in any of the eight directions (left, right, up, down, or the four diagonals). There are K obstacles on the chessboard preventing the queen from attacking any square that has an obstacle blocking the the queen's path to it. Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (rq, cq)

#!/bin/python3

import sys

total = 0
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

hObstacle = [0, n + 1]
vObstacle = [n + 1 ,0]
pSlope = [rQueen - min(cQueen - 1, rQueen - 1) - 1, rQueen + min(n - rQueen, n - cQueen) + 1]
nSlope = [rQueen + min(cQueen - 1, n - rQueen) + 1, rQueen - min(rQueen - 1, n - cQueen) - 1]

for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    
    rDif = rObstacle - rQueen
    cDif = cObstacle - cQueen
    
    if(rObstacle == rQueen):
        if(cObstacle < cQueen):
            hObstacle[0] = cObstacle
        else:
            hObstacle[1] = cObstacle
    elif(cObstacle == cQueen):
        if(rObstacle > rQueen):
            vObstacle[0] = rObstacle
        else:
            vObstacle[1] = rObstacle
    elif(abs(rDif) == abs(cDif)):
        if(pSlope[0] < rObstacle and rDif < 0 and cDif < 0):
            pSlope[0] = rObstacle
        elif( pSlope[1] > rObstacle and rDif > 0 and cDif > 0):
            pSlope[1] = rObstacle
        elif(nSlope[0] > rObstacle and rDif > 0 and cDif < 0):
            nSlope[0] = rObstacle
        elif(nSlope[1] < rObstacle and rDif < 0 and cDif > 0):
            nSlope[1] = rObstacle
 
total += abs(pSlope[0] - pSlope[1]) - 2
total += abs(nSlope[0] - nSlope[1]) - 2

total += abs(hObstacle[0] - hObstacle[1]) - 2
total += abs(vObstacle[0] - vObstacle[1]) - 2

print(total)
