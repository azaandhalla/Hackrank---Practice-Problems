#Given a set, S, of n distinct integers, print the size of a maximal subset, S', of S where the sum of any 2 numbers in S' is not evenly divisible by k.

n,k = map(int,input().split(" "))
array = input().split(" ")
matrix = [0 for x in range(int(k))] 


for i in array:
    matrix[int(i) % int(k)] += 1
    #print(i , " " , int(i) % int(k) , " ", matrix[int(i) % int(k)])
        
count = min(matrix[0], 1);
for i in range(1, int(k/2)+1):
    if(i != int(k) - i):
        count += max(matrix[i], matrix[k-i])
        
if(k % 2 == 0):
    count += min(matrix[int(k/2)], 1)
    
        
print(count)
