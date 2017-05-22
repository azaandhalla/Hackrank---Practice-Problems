'''Alice and Bob are playing the following game:
- The game starts with a sequence of zeroes and ones.
- Alice and Bob take alternating turns, and Alice always moves first.
- During each turn, a player removes one element from the sequence that satisfies the following:
- It is not the first or last element.
- It must be surrounded by zeroes on both sides.
- The first player who can't take their turn loses the game.
- Both players always move optimally.'''

import sys

g = int(input().strip())
count = 0
for a0 in range(g):
    n = int(input().strip())
    a = list(map(str, input().strip().split(' ')))
    for x in range(1, len(a) - 1):
        value = int(a[x - 1]+a[x]+a[x + 1], 2)
        if value == 0 :
            count += 1
        elif value == 1 and x + 2 <= len(a) - 1 and a[x + 2] == '0' :
            count += 1
        elif value == 2 :
            a[x] = '0'
            count += 1
        
    if count % 2 == 0:
        print("Bob")
    else:
        print("Alice")
    count = 0
