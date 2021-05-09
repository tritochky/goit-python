import datetime
from collections import defaultdict


def congratulate(users):
    current_day = datetime.date.today()
    current_week = current_day.isocalendar().week
    
    for user in users:
        fun_day = user['birthday']
        fun_day = fun_day.replace(2021)
        fun_week = fun_day.isocalendar().week
        
        if fun_week == current_week + 1:
            day_of_week = day_of_week = fun_day.weekday()
                         
            if day_of_week == 0:
                children_of_mon.append(user['name'])
            elif day_of_week == 1:
                children_of_tue.append(user['name'])
            elif day_of_week == 2:
                children_of_wed.append(user['name'])
            elif day_of_week == 3:
                children_of_thu.append(user['name'])
            elif day_of_week == 4:
                children_of_fri.append(user['name'])
            elif day_of_week == 5 or day_of_week == 6:
                children_of_mon.append(user['name'])

        schedule = defaultdict(list)
        schedule = [{'Monday': children_of_mon},
                    {'Tuesday': children_of_tue},
                    {'Wednesday': children_of_wed},
                    {'Thursday': children_of_thu},
                    {'Friday': children_of_fri}]

    for elem in schedule:
        for key, value in elem.items():
            if len(value) != 0:
                gays = ', '.join(value)
                value = gays
                print(key, ': ', value)
    return



users = [{'name': 'Kate', 'birthday': datetime.date(year=2004, month=1, day=6)},
         {'name': 'Nike', 'birthday': datetime.date(year=2008, month=11, day=20)},
         {'name': 'Jack', 'birthday': datetime.date(year=2017, month=5, day=14)},
         {'name': 'Anne', 'birthday': datetime.date(year=2009, month=11, day=30)},
         {'name': 'Bill', 'birthday': datetime.date(year=2003, month=9, day=25)},
         {'name': 'Hank', 'birthday': datetime.date(year=2010, month=12, day=7)},
         {'name': 'Bella', 'birthday': datetime.date(year=1995, month=10, day=31)},
         {'name': 'Suga', 'birthday': datetime.date(year=1996, month=3, day=9)},
         {'name': 'Goock', 'birthday': datetime.date(year=1999, month=9, day=1)},
         {'name': 'Tom', 'birthday': datetime.date(year=1999, month=5, day=10)},
         {'name': 'Jane', 'birthday': datetime.date(year=1999, month=5, day=13)},
         {'name': 'Lise', 'birthday': datetime.date(year=1999, month=5, day=17)},
         {'name': 'Luise', 'birthday': datetime.date(year=1999, month=5, day=13)}]
children_of_mon = []
children_of_tue = []
children_of_wed = []
children_of_thu = []
children_of_fri = []

    
def main():
    congratulate(users)


if __name__ == '__main__':
    main()
