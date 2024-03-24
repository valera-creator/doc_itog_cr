import json

# чтение из js
with open('file.json', mode='r') as file:
    info = json.load(file)
    print(info)

# запись в json
# урок WEB. Работа с файловой системой и популярными форматами файлов: zip-архивами и json-файлами, параграф 7
data = [{1: 2, 3: 4}]
with open('file.json', mode='w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
