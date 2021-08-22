import os

lines = []


def open_stonks():
    if 'stonks.txt' in os.listdir() and 'not_stonks.txt' in os.listdir():
        try:
            f = open('stonks.txt', 'r')
            lines = f.readlines()
            f.close()
            return lines
        except:
            print(45)


def open_not_stonks():
    if 'stonks.txt' in os.listdir() and 'not_stonks.txt' in os.listdir():
        try:
            f = open('not_stonks.txt', 'r')
            lines = f.readlines()
            f.close()
            return lines
        except:
            print(45)
