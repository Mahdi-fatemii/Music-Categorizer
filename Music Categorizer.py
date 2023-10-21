import re
import os
import csv
from Music_Categorizer_funcs import *
import openpyxl

theFile = openpyxl.load_workbook('hard-rock.xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))

music_name = 'Gho'
for x in allSheetNames:
    print("Current sheet name is {}" .format(x))
    currentSheet = theFile[x]
    for i in range(1,346):
        sheet = f'A{i}'
        if currentSheet[sheet].value == music_name:
            
            print(currentSheet[sheet].value, True)

mpath = "C:\\Users\\MT1ShotYT\\Desktop\\music"

 
# file = open("C:\\Users\\MT1ShotYT\\Desktop\\Music-Categorizer\\Music-Categorizer\\DB\\hard-rock.csv", "r")
