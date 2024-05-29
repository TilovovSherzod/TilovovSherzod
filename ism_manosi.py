import json

# JSON faylini o'qish
file_path = 'ismlar_manosi.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Ma'lumotlarni dictionary shaklida o'zgartirish(tezlik uchun)
data_dict = {item['properties']['name'].lower(): item for item in data}

# Ismni qidirish funksiyasi
def find_name(name):
    return data_dict.get(name.lower(), None)