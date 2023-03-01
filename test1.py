# 1
# def process_string(l, t):
#     ans = []
#     for i in range(len(l)):
#         if l[i][0] == t[0]:
#             ans.append(l[i])
#     print(ans)
#
# def process_numeric(l, t):
#     ans = []
#     for i in range(len(l)):
#         if int(l[i]) > int(t):
#             ans.append(l[i])
#     print(ans)
#
#
# s = list(input().split())
# t = input()
#
# if s[0].isdigit():
#     process_numeric(s, t)
# else:
#     process_string(s, t)


# 2
# def WhatWillDo(instance, time):
#     print("He will {} at {}".format(instance.affairs[time], time))
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def inroduce(self):
#         print(self.name, self.surname)
#
#
# class Student(Person):
#     def __init__(self, name, surname, affairs):
#         super().__init__(name, surname)
#         self.affairs = affairs
#
#
# class Employee(Person):
#     def __init__(self, name, surname, affairs):
#         super().__init__(name, surname)
#         self.affairs = affairs
#
#
# st1 = Student("Mark", "Twen", {0: "sleep", 6: "get up", 8: "study", 13: "luch", 14: "do homework"})
#
# WhatWillDo(st1, 8)


# 3
# class Piece:
#     def __init__(self, position = "A1"):
#         self.position = position
#     def setPosition(self):
#         position = ""
#         while len(position) == 0:
#             newPos = input("Write the position of the piece:\n")
#             if (int(newPos[1]) >= 0 and int(newPos[1]) <= 8) and (ord(newPos[0]) >= 65 and ord(newPos[0]) <= 72):
#                 position = newPos
#                 self.position = position
#     def getPosition(self):
#         print("The position is {}".format(self.position))
#
# class Rook(Piece):
#     def isLegal(self, newPos):
#         if self.position[0] == newPos[0] or self.position[1] == newPos[1]:
#             return True
#         return False
#
# class Queen(Piece):
#     def isLegal(self, newPos):
#         if self.position[0] == newPos[0] or self.position[1] == newPos[1]:
#             return True
#         elif abs(ord(self.position[0]) - ord(newPos[0])) == abs(int(self.position[1]) - int(newPos[1])):
#             return True
#         return False
#
# class Pawn(Piece):
#     def isLegal(self, newPos):
#         if self.position[0] != newPos[0]:
#             return False
#         elif (self.position[1] == "2" or self.position[1] == "7") and (abs(int(self.position[1]) - int(newPos[1])) <= 2):
#             return True
#         elif abs(int(self.position[1]) - int(newPos[1])) == 1:
#             return True
#         return False
#
# class Knight(Piece):
#     pass
#
# paw = Pawn()
# paw.setPosition()
#
# print(paw.isLegal("B4"))
#
# queen = Queen()
# queen.setPosition()
#
# print(queen.isLegal("G7"))
#
# rook = Queen()
# rook.setPosition()
#
# print(rook.isLegal("E7"))