len_1 = 0; len_2 = 0; len_3 = 0; file_1 = []; file_2 = []; file_3 = []

with open('1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        len_1 += 1
        file_1.append(line.strip())
with open('2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        len_2 += 1
        file_2.append(line.strip())
with open('3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        len_3 += 1
        file_3.append(line.strip())
with open('all_in_one.txt', 'a', encoding='utf-8') as f:
    f.write(f'Файл 2.txt\nВ нем {len_2} строк(а)\n')
    for n in file_2:
        f.write(f'{n}\n')
    f.write(f'\nФайл 1.txt\nВ нем {len_1} строк(а)\n')
    for n in file_1:
        f.write(f'{n}\n')
    f.write(f'\nФайл 3.txt\nВ нем {len_3} строк(а)\n')
    for n in file_3:
        f.write(f'{n}\n')

# Цитата из задания: Считайте, что их количество и имена вам заранее известны
# т.е. мне не нужно проводить махинации с определением порядка, так ведь?