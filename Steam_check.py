import os, re, subprocess, time

directory_path = ['D:\SteamLibrary\steamapps', 'D:\games\steam\steamapps', 'E:\steam\steamapps', 'F:\steam\steamapps']

def search_steam_id(steam_directory):
    file_names = []
    try:
        for filename in os.listdir(steam_directory):
            if filename.endswith('.acf'):
                filename = re.sub(r"\D", "", filename)
                file_names.append(filename)
    except OSError:
        print(f"Директория '{steam_directory}' не найдена")
    return file_names

def file_Integrity_Check(app_id):
    subprocess.call(["explorer.exe", f"steam://validate/{app_id}"])
    time_to_check = 0
    log_file_path = "C:\\Program Files (x86)\\Steam\\logs\\content_log.txt"
    while True:
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as log_file:
                log_content = log_file.read()
                if re.search(rf"AppID {app_id} update changed : None", log_content):
                    break
        time.sleep(10)
        time_to_check += 10
    a = f'{app_id} - проверка завершена, длительность {time_to_check // 60} мин. {time_to_check % 60} сек.'
    print(a)
    return a

all_game_id = []

os.system("taskkill /F /IM steam.exe")
time.sleep(3)

for i in directory_path:
    all_game_id.extend(search_steam_id(i))

print(f'Найдено игр: {len(all_game_id)}. Список: {all_game_id}')

os.remove("C:\\Program Files (x86)\\Steam\\logs\\content_log.txt")

result_check = []
for i in all_game_id:
    result_check.append(file_Integrity_Check(i))

with open('log.txt', 'w') as file:
    for item in result_check:
        file.write("%s\n" % item)

print("Проверка завершена")
