import m1, main
from datetime import datetime

class lesson:
    def __init__(self):
        self.name = "CLASS LESSON"
        self.date = "16-02-2023"


x = int(input())
names_of_the_lists = m1.generate_dates(datetime.today(), main.get_random(x))