from datetime import datetime

def get_random(x):
    cur = int(datetime.utcnow().timestamp())
    if cur / x % 10 == 0:
        return 1
    else:
        return int(cur / x % 10)


# x = int(input())
# print(get_random(x))