# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме:
# по десять пар "код-символ" в каждой строке.

if __name__ == '__main__':

    def build_table(start, stop):

        for i in range(0, 10):
            if start > stop:
                return
            print(ord(chr(start)), chr(start), end=' ')
            start += 1
        print('')
        build_table(start, stop)


    build_table(32, 127)


# FIN
