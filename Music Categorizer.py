from Music_Categorizer_funcs import *

folder_path = "C:\\Users\\MT1ShotYT\\Desktop\\music"

while True:
    print(f'{"*"*50}\n1: Blues\n2: Country\n3: Folk\n4: Hip Hop\n5: Jazz\n6: Pop\n7: R&B\n8: Rock\n9: Metal\n10: Punk\n11: Persian\n12: Rock & Roll\n13: Electronic\n15: EXIT\n{"*"*50}') #12:\n13:\n14:
    check = input('please select a Genre:')
    if check == '1':
            # Blues
        music_categorizer(folder_path, db_file_name='All_Blues.xlsx', folder_name='All_Blues')
        continue
    elif check == '2':
           # country
        music_categorizer(folder_path, db_file_name='country.xlsx', folder_name='country')
        continue
    elif check == '3':
        pass
    elif check == '4':
        pass
    elif check == '5':
        # jazz
        music_categorizer(folder_path, db_file_name='jazz.xlsx', folder_name='jazz')
        continue
    elif check == '6':
        print(f'{"*"*50}\n1: Pop\n2: indie-pop\n3: BACK\n{"*"*50}')
        check = input('please choose the option:')
        if check == '1':
            # pop
            music_categorizer(folder_path, db_file_name='pop.xlsx', folder_name='pop')
            continue
        elif check == '2':  
            # indie-pop  
            music_categorizer(folder_path, db_file_name='indie-pop.xlsx', folder_name='indie-pop')
            continue
        elif check == '3':  
            break     
    elif check == '7':
        pass
    elif check == '8':
        print(f'{"*"*50}\n1: hard-rock\n2: soft-rock\n3: alternative-rock\n4: garage-rock\n5: indie-rock\n6: post-rock\n7: rap-rock\n8: BACK\n{"*"*50}')
        check = input('please choose the option:')
        if check == '1':
           # hard-Rock
            music_categorizer(folder_path, db_file_name='hard-rock.xlsx', folder_name='hard-rock')
            continue
        elif check == '2':
            # soft-rock
            music_categorizer(folder_path, db_file_name='soft-rock.xlsx', folder_name='soft-rock')
            continue
        elif check == '3':
            # alternative-rock
            music_categorizer(folder_path, db_file_name='alternative-rock.xlsx', folder_name='alternative-rock')
            continue
        elif check == '4':
            # garage-rock
            music_categorizer(folder_path, db_file_name='garage-rock.xlsx', folder_name='garage-rock')
            continue
        elif check == '5':
            # indie-rock
            music_categorizer(folder_path, db_file_name='indie-rock.xlsx', folder_name='indie-rock')
            continue
        elif check == '6':
            # post-rock
            music_categorizer(folder_path, db_file_name='post-rock.xlsx', folder_name='post-rock')
            continue
        elif check == '7':
            music_categorizer(folder_path, db_file_name='rap-rock.xlsx', folder_name='rap-rock')
            continue
        elif check == '8':
            break 
    elif check == '9':
        music_categorizer(folder_path, db_file_name='heavy-metal.xlsx', folder_name='heavy-metal')
        continue
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
        elif check == '4':
            music_categorizer(folder_path, db_file_name='Iran-classical.xlsx', folder_name='Iran-classical')
            continue
    elif check == '12':
        music_categorizer(folder_path, db_file_name='rock-and-roll.xlsx', folder_name='rock-and-roll')
        continue
    elif check == '13':
        pass
    elif check == '14':
        pass
    elif check == '15':
        break