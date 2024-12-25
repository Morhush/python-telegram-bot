import random
from webbrowser import open_new

filename = 'f1.txt'

# запис
# with open(filename, 'w') as f:
#     f.write('New text!')

# зчитування
# with open(filename, 'r') as f:
#     text = f.read()
#     print(text)

# f = open(filename, 'r')
# try:
#     text = f.read()
#     print(text)
# finally:
#     f.close()
#     print('End!')

#1
# with open(filename, 'w') as file:
#     for n in range(0, 10):
#         file.write(str(random.randint(-10, 10)) + '\n')
#
# with open(filename, 'r') as file:
#     number = file.read()
#     while number:
#         print(number)
#         number = file.readline()
#     #      print(number)

# filename = 'f8.txt'
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write('Text utf-8.')
# with open(filename, 'r', encoding='utf-8') as file:
#     print(file.read('Text utf-8.'))

# filename = 'b1.txt'
# with open(filename, 'ab') as file:
#     file.write(b"\x4E\x4E\x4E\x4E")
# with open(filename, 'rb') as file:
#     content = file.readline()
#     print(content)

