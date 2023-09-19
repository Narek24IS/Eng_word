import pyautogui
from random import shuffle
from time import sleep

# 1 - с русского на английский 0 - с английского на русский
revers = 1

lst = []
with open('input.txt', 'r') as ifile:
    # noinspection PyRedeclaration
    for line in ifile:
        line = line.replace('–', '-')
        lst.append((x.strip() for x in line.split('-')))

shuffle(lst)
sleep(0.3)
pyautogui.click(x=69, y=942)

if revers:
    for eng, rus in lst:
        print(rus, end='')
        input()
        print(eng)
        input()
        pyautogui.click(x=69, y=942)
else:
    for eng, rus in lst:
        print(eng, end='')
        input()
        print(rus)
        input()
        pyautogui.click(x=69, y=942)

