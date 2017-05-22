'''An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the following constraints:
For example, the sentence "if man was meant to stay on the ground god would have given us roots" after removing spaces is  characters long, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message in English with no spaces between the words. 
'''
import sys
import math


s = input().strip()
row = math.floor(math.sqrt(len(s)))
col = math.ceil(math.sqrt(len(s)))

if((col * row) < len(s)):
    row += 1

for i in range(0, col):
    for j in range(0, row):
        try:
            print(s[i + j * col], end="")
        except IndexError:
            continue
    print(" ", end="")
