import os


def del_all():
    os.remove('stonks.txt')
    os.remove('not_stonks.txt')
    return 'Успешно'


def create_txts():
    if 'stonks.txt' not in os.listdir() or 'not_stonks.txt' not in os.listdir():
        try:
            f = open("stonks.txt", 'w')
            f.close()
            f = open("not_stonks.txt", 'w')
            f.close()

        except:
            return 'Error'
        return 'Secuss'


def append_stonks(name, sum, day):
    if 'stonks.txt' in os.listdir():
        f = open("stonks.txt", 'a')
        f.write(name + ':' + sum + '@' + day + '\n')
        f.close()

        return 'Успешно'


def append_not_stonks(name, sum, day):
    if 'not_stonks.txt' in os.listdir():
        f = open("not_stonks.txt", 'a')
        f.write(name + ':' + sum + '@' + day + '\n')
        f.close()

        return 'Успешно'
