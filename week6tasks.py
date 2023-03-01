import re

# 1
# s = input()
# print(re.findall('\S+@\S+', s))


# 2
# s = input()
#
# if re.search('mail.ru', s):
#     print(re.sub('mail.ru', 'gmail.com', s))
# if re.search('yahoo.com', s):
#     print(re.sub('yahoo.com', 'outlook.com', s))
# if re.search('bk.ru', s):
#     print(re.sub('bk.ru', 'kbtu.kz', s))

# amir@mail.ru amir@yahoo.com amir@bk.ru


# 3
# s = input()
#
# if 8 <= len(s) <= 15:
#     if re.search('[a-z]', s):
#         if re.search('^[a-z]', s):
#             if re.search('\d', s):
#                 if re.search('qwerty', s) or re.search('asd', s) or re.search('QWERTY', s) or re.search('ASD', s):
#                     print("incorrect 5")
#                 else:
#                     print("correct")
#             else :
#                 print("incorrect 4")
#         else:
#             print("incorrect 3")
#     else:
#         print("incorrect 2")
# else:
#     print("incorrect 1")

