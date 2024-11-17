import os

def acounting(file:str):
    return sum(1 for _ in open('1.txt', 'r', encoding='utf-8'))

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        if i.endswith('.txt'):
            files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a') # Сюда записываем
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r', encoding = 'utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


file_for_writing = os.path.abspath('result.txt') # Сюда записываем результат. 
base_path = os.getcwd()
location = os.path.abspath('.')
rewriting(file_for_writing, base_path, location) 

  