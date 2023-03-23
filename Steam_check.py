import os, re, subprocess, pyautogui, time

directory_path = ['D:\Games\steam\steamapps', 'E:\steam\steamapps', 'F:\steam\steamapps']

def search_steam_id(steam_directory):
    file_names = []
    try:
        for filename in os.listdir(steam_directory):
            if filename.endswith('.acf'):
                filename = re.sub(r"\D", "", filename)
                file_names.append(filename)
    except OSError:
        print(f"Директория '{steam_directory}' Не найдена")
    return file_names

def file_Integrity_Check(app_id):
    subprocess.call(["explorer.exe", f"steam://validate/{app_id}"])
    button_location = None
    time_to_check = 0
    while button_location is None:
        button_location = pyautogui.locateOnScreen('button.png')
        if button_location is None:
            time.sleep(10)
            time_to_check+=10
    pyautogui.click(button_location)
    pyautogui.moveRel(100, 100, 2)
    a = f'{app_id} - проверка завершена, длительность {time_to_check//60} мин. {time_to_check%60} сек.'
    print(a)
    return a

all_game_id = []

for i in directory_path:
    all_game_id.extend(search_steam_id(i))

print(f'Найдено {len(all_game_id)} игр. Список: {all_game_id}')

result_check = []
for i in all_game_id:
    result_check.append(file_Integrity_Check(i))

with open('log.txt', 'w') as file:
    for item in result_check:
        file.write("%s\n" % item)
