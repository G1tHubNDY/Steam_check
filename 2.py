result_check = ['1145360 - проверка завершена, длительность 0 мин. 10 сек.', '1220140 - проверка завершена, длительность 0 мин. 0 сек.', '1222670 - проверка завершена, длительность 0 мин. 10 сек.', '1432050 - проверка завершена, длительность 0 мин. 0 сек.', '282070 - проверка завершена, длительность 0 мин. 0 сек.', '289070 - проверка завершена, длительность 0 мин. 0 сек.', '322330 - проверка завершена, длительность 0 мин. 0 сек.', '323190 - проверка завершена, длительность 0 мин. 0 сек.', '413150 - проверка завершена, длительность 0 мин. 0 сек.', '457140 - проверка завершена, длительность 0 мин. 0 сек.', '588650 - проверка завершена, длительность 0 мин. 0 сек.', '632360 - проверка завершена, длительность 0 мин. 10 сек.', '648800 - проверка завершена, длительность 0 мин. 0 сек.', '746850 - проверка завершена, длительность 0 мин. 0 сек.', '846770 - проверка завершена, длительность 0 мин. 0 сек.', '881100 - проверка завершена, длительность 0 мин. 0 сек.', '892970 - проверка завершена, длительность 0 мин. 0 сек.', '8930 - проверка завершена, длительность 0 мин. 0 сек.']

with open('file.txt', 'w') as file:
    for item in result_check:
        file.write("%s\n" % item)
