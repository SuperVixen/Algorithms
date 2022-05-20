# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

def kogo_6olwe():
    lst = [randint(1, 30) for i in range(20)]
    lsst = {i:0 for i in lst}
    print(lst)
    for x in lst:
        lsst[x] += 1

    max_lst = max(lsst.values())
    return print('Больше всего', max(lsst, key=lsst.get), '- их', max_lst, 'штук')

if __name__ == '__main__':
    kogo_6olwe()
# FIN
