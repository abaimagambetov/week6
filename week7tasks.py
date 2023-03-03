import os

# 1
# s = input()
# print(os.listdir(s))


# 2
# s = input("Enter the name of the file: ")
# s += ".txt"
# f = open(s, 'r')
# x = f.read()
#
# print("Content from the file:", x)
# print("Number of characters:", len(x))
#
# cnt = 0
#
# for i in x:
#     if i == '=':
#         cnt += 1
#
# print("Number of '=' signs:", cnt)


# 3
with open('input.txt', 'r') as file:
    data = file.readlines()

n = int(input("Which line do you want to change? "))
new_line = input("New line: ")

if new_line == "***":
    print("fault")
else:
    data[n] = new_line + '\n'
    with open('input.txt', 'w') as file:
        file.writelines(data)

f = open("input.txt", 'r')
print(f.read())




