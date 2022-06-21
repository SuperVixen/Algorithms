# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

def substring_count(string):

    hash_set = set()

    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            # print(h)
            hash_set.add(h)
    return len(hash_set)

if __name__ == '__main__':

    some_str = str(input('Введите строку из маленьких латинских букв: ')).lower()
    print('Количество различных подстрок в строке ', some_str, ': ', substring_count(some_str))

# FIN
