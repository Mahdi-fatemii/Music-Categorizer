import os
import re

file = open('C:\\Users\\MT1ShotYT\\Desktop\\Music-Categorizer\\Music-Categorizer\\DB\\Rock\\rap-rock.txt', 'r') 
lst = []
lst = file.readlines()
lst2 = []
for i in lst:
    name = ''
    for j in i:
        if j == "[" : 
            break
        else:
            name += j
    if len(name) == 1:
        break
    else:
        if name != '':
            lst2.append(name)

# for reamoving blank lines 
lst3 = []
for i in lst2:
    x = re.sub("\n", " ",i)
    lst3.append(x)
    
# creating and writing anew txt file
filex = open('alter-1.txt', 'a') 
for line in lst3:
    filex.write(line)
    filex.write('\n')
print("done")
