'''Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater 
than w. In case of multiple possible answers, find the lexicographically smallest one among them.'''


for x in range(int(input().strip())):
    s = input().strip()
    x = len(s) - 1
    while(x > 0 and s[x] <= s[x - 1]):
        x -= 1
        
    if(x == 0):
        print("no answer")
        continue
    
    j = len(s) - 1
    while(j > x - 1 and s[j] <= s[x - 1]):
        j -= 1
    
    s = list(s)
    s[x - 1], s[j] = s[j], s[x - 1]
    print(''.join(s[:x]) + ''.join(list(reversed(s[x:]))))
