import os
import re

file = open('C:\\Users\\mm\\Desktop\\New folder\\Music-Categorizer\\DB\\Jazz\\jazz.txt', 'r') 
lst = []
lst = file.readlines()
lst2 = []
for i in lst:
    name = ''
    for j in i:
        if j == "(" : 
            break
        else:
            
            name += j
    if len(name) == 1:
        break
    else:
        lst2.append(name)
filex = open('jazz.txt', 'a') 
for line in lst2:
    filex.write(line)
    filex.write('\n')

print("done")
