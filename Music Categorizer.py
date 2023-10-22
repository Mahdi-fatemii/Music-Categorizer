from Music_Categorizer_funcs import *

folder_path = "C:\\Users\\MT1ShotYT\\Desktop\\music"
# Rock
music_categorizer(folder_path, db_file_name='hard-rock.xlsx', folder_name='hard-rock')
# Blues
music_categorizer(folder_path, db_file_name='All_Blues.xlsx', folder_name='All_Blues')
# Persian
music_categorizer(folder_path, db_file_name='Iran-Pop.xlsx', folder_name='Iran-Pop')
music_categorizer(folder_path, db_file_name='Iran-hip-hop.xlsx', folder_name='Iran-hip-hop')
music_categorizer(folder_path, db_file_name='Iran-classical.xlsx', folder_name='Iran-classical')
