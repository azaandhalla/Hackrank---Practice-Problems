In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, S. You must perform Q operations of the following  types:

append(W) - Append string W to the end of s.
delete(k) - Delete the last k characters of s.
print(k) - Print the kth character of s.
undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

import sys

s = []
history = []
for j in range(int(input().strip())):
    x = input().strip().split(' ')
    if x[0] == '1':
        s += list(x[1])
        history.append(len(x[1]))
    elif x[0] == '2':
        history.append(s[-int(x[1]):])
        s = s[:-int(x[1])]
    elif x[0] == '3':
        print(s[int(x[1]) - 1])
    else:
        undo = history.pop()
        if str(undo).isdigit():
            s = s[:-int(undo)]
        else:
            s += undo
