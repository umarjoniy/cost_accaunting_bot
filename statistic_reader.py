import filereader


def read_for_stonks(day, state_of_workink):
    dict1 = {}
    list_for_rasxodov = []

    if state_of_workink == 1:
        """Тогда, когда пользователь хочет получить стату за день"""
        list = filereader.open_stonks()
        # Пенсия:213@10 02 2002
        for i in list:
            if day == i[i.find("@") + 1:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1

    elif state_of_workink == 2:
        """Тогда, когда пользователь хочет получить стату за месяц"""
        list = filereader.open_stonks()
        for i in list:
            if day == i[i.find("@") + 4:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1

    elif state_of_workink == 3:
        """Тогда, когда пользователь хочет получить стату за год"""
        list = filereader.open_stonks()
        for i in list:
            if day == i[i.find("@") + 7:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1


def read_for_not_stonks(day, state_of_workink):
    dict1 = {}
    list_for_rasxodov = []

    if state_of_workink == 1:
        """Тогда, когда пользователь хочет получить стату за день"""
        list = filereader.open_not_stonks()
        # Пенсия:213@10 02 2002
        for i in list:
            if day == i[i.find("@") + 1:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1

    elif state_of_workink == 2:
        """Тогда, когда пользователь хочет получить стату за месяц"""
        list = filereader.open_not_stonks()
        for i in list:
            if day == i[i.find("@") + 4:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1

    elif state_of_workink == 3:
        """Тогда, когда пользователь хочет получить стату за год"""
        list = filereader.open_not_stonks()
        for i in list:
            if day == i[i.find("@") + 7:len(i) - 1]:
                name = i[0:i.find(":")]
                summa = int(i[i.find(":") + 1:i.find("@")])
                if name not in list_for_rasxodov:
                    dict1[name] = 0
                    list_for_rasxodov.append(name)
                dict1[name] = dict1.get(name) + summa
        return dict1


def ostatok(day, state_of_workink):
    total_stonks = 0
    if state_of_workink == 1:
        """Тогда, когда пользователь хочет получить остаток за день"""
        list = filereader.open_stonks()
        # Пенсия:213@10 02 2002
        for i in list:
            if day == i[i.find("@") + 1:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks + summa

        list = filereader.open_not_stonks()
        for i in list:
            if day == i[i.find("@") + 1:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks - summa
        return total_stonks

    elif state_of_workink == 2:
        """Тогда, когда пользователь хочет получить остаток за месяц"""
        list = filereader.open_stonks()
        # Пенсия:213@10 02 2002
        for i in list:
            if day == i[i.find("@") + 4:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks + summa

        list = filereader.open_not_stonks()
        for i in list:
            if day == i[i.find("@") + 4:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks - summa
        return total_stonks

    elif state_of_workink == 3:
        """Тогда, когда пользователь хочет получить остаток за месяц"""
        list = filereader.open_stonks()
        # Пенсия:213@10 02 2002
        for i in list:
            if day == i[i.find("@") + 7:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks + summa

        list = filereader.open_not_stonks()
        for i in list:
            if day == i[i.find("@") + 7:len(i) - 1]:
                summa = int(i[i.find(":") + 1:i.find("@")])
                total_stonks = total_stonks - summa
        return total_stonks
