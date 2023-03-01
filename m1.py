import main
from datetime import timedelta, datetime

def generate_dates(t, r):
    l = [datetime.strftime(t + timedelta(i), '%Y-%m-%d') for i in range(1, r + 1)]
    return l


# x = int(input())
# print(generate_dates(datetime.today(), main.get_random(x)))