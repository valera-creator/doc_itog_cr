import csv

# чтение из csv
with open('file.csv', encoding="utf8") as csvfile:  # урок pyqt6, параграф 6
    reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))[1:]  # отрезаем заголовки, delimiter - разделитель
    print(reader)

# Запись
# Работа с простыми таблицами (csv). Работа с табличными данными в PyQT, параграф 6
with open('file.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for elem in [['first', 'second'], [1, 2]]:
        writer.writerow(elem)
