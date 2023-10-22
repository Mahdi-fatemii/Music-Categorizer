from Music_Categorizer_funcs import *

folder_path = "C:\\Users\\MT1ShotYT\\Desktop\\music"
while True:
    print(f'{"*"*50}\n1: Blues\n2: Country\n3: Folk\n4: Hip Hop\n5: Jazz\n6: Pop\n7: R&B\n8: Rock\n9: Metal\n10: Punk\n11: persian\n\n15: EXIT\n{"*"*50}') #12:\n13:\n14:
    check = input('please select a Genre:')
    if check == '1':
     # Blues
        music_categorizer(folder_path, db_file_name='All_Blues.xlsx', folder_name='All_Blues')
        continue
    elif check == '2':
        pass
    elif check == '3':
        pass
    elif check == '4':
        pass
    elif check == '5':
        pass
    elif check == '6':
        pass
    elif check == '7':
        pass
    elif check == '8':
           # hard-Rock
        music_categorizer(folder_path, db_file_name='hard-rock.xlsx', folder_name='hard-rock')
        continue
    elif check == '9':
        pass
    elif check == '10':
        pass
    elif check == '11':
        # Persian
        print(f'{"*"*50}\n1: Pop\n2: Hip hop\n3: Old/Classical\n4: BACK\n{"*"*50}')
        check = input('please choose the option:')
        if check == '1':
            # Persian-pop
            music_categorizer(folder_path, db_file_name='Iran-Pop.xlsx', folder_name='Iran-Pop')
            continue
        elif check == '2':  
            # Persian-hiphop  
            music_categorizer(folder_path, db_file_name='Iran-hip-hop.xlsx', folder_name='Iran-hip-hop')
            continue
        elif check == '3':  
            # Persian-old\classical  
            music_categorizer(folder_path, db_file_name='Iran-classical.xlsx', folder_name='Iran-classical')
            continue        
    elif check == '12':
        pass
    elif check == '13':
        pass
    elif check == '14':
        pass
    elif check == '15':
        break