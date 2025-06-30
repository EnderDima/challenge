import calendar
import datetime
#import time

data = datetime.datetime.today()
year = data.year
month = data.month
print('Сообщение появится через 5 сек')
#time.sleep(5)
print(calendar.month(year, month))

def day_week(data):
    day_of_week = data.weekday()
    weekday = data.strftime("%A")
    if day_of_week == 5 or day_of_week == 6:
        print('Сегодня выходной!', weekday)
    else:
        print('Сегодня рабочий день.', weekday)

day_week(data)
