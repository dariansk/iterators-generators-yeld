from generator import hash_file
from iterator import Countries


if __name__ == '__main__':
    countries = Countries('countries.json')
    with open('links.txt', 'w') as new_file:
        for country in countries:
            new_file.write(f'{country}\n')

    for number, hash_line in enumerate(hash_file(input('Введите путь к файлу: ')), 1):
        print(f'{number}: {hash_line}')