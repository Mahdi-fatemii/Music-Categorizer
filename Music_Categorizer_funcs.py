import re
import os
import openpyxl

folder_path = "C:\\Users\\MT1ShotYT\\Desktop\\music"


def all_files_list(folder_path):
    mpath = folder_path
    files = [f for f in os.listdir(mpath)]
    return files


def music_name_finder(files):
    artists_names_list = []
    for musicname in files:
        if len(musicname) > 0 :
            x = musicname.split('-')
            c = ''
            counter = 0
            for i in x[0]:
                if i == '.':
                    break
                else:
                    if i.isalpha() or i == ' ':
                        if i == ' ' and counter <= 1:
                            pass
                        else:    
                            c += i
                            counter += 1
                            if counter >= 30:
                                break
                    else:
                        continue
            artists_names_list.append(c)
    return artists_names_list
                

def folder_creation(path, name):
    main_dir = path + '\\' + name
    # Check if folder does not already exist
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
        print(f"Created folder '{main_dir}'.")
    else:
        print(f"Folder '{main_dir}' already exists.")
        
        
def all_music_fullname_finder(folder_path):
    files = all_files_list(folder_path)
    lst = music_name_finder(files)
    for i in range(len(lst)):
        for j in  range(len(files)):
            if lst[i] in files[j]:
                print(lst[i])
                print(files[j])
                
                
def music_fullname_finder(folder_path, name):         
    files = all_files_list(folder_path)
    for j in  range(len(files)):
        if name in files[j]:
            music_name = files[j]
            return music_name
            

def path_definer(movefrom, moveto, music_name):
    movefrom = movefrom + '\\' + music_name
    moveto = moveto + '\\' + music_name
    
    return movefrom, moveto
    
            
def move_music_to_directory(movefrom, moveto):
    os.rename(movefrom, moveto)
    print('done')
    

def DB_Music_Name_Check(file_name, music_name):
    theFile = openpyxl.load_workbook(file_name)
    allSheetNames = theFile.sheetnames
    
    for x in allSheetNames:
        currentSheet = theFile[x]
        for i in range(1,346):
            sheet = f'A{i}'
            if currentSheet[sheet].value == music_name:
                return True
            else:
                return False