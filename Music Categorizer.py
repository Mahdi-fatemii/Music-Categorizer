import re
import os
import csv
from Music_Categorizer_funcs import *
import openpyxl
import eyed3

folder_path = "C:\\Users\\MT1ShotYT\\Desktop\\music"
   
music_categorizer(folder_path, db_file_name='hard-rock.xlsx', folder_name='hard-rock')


