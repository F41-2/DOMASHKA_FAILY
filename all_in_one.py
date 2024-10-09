import os
os.chdir('allinone')
len_f = 0; file = {}
if os.path.exists("all_in_one.txt"):
    print('Файл уже объединялся')
else:
    for x in os.listdir():
        if x.endswith(".txt"):
            with open(x, 'r', encoding='utf-8') as f:
                for line in f:
                    len_f += 1
                file[len_f] = x
                len_f = 0
            sorted_file = sorted(((k,v) for k, v in file.items()), reverse=False)

    for m in sorted_file:
        name = m[1]
        with open('all_in_one.txt', 'a', encoding='utf-8') as x:
            x.write(f'\n{m[1]}\nВ нем {m[0]} строк(а)\n\n')
            with open(name, 'r', encoding='utf-8') as j:
                for line in j:
                    x.write(f'{line.strip()}\n')