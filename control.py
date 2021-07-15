import pyautogui as py
from random import randint
size = py.size()
x = size[0]
y = size[1]
for i in range(100):
	py.moveTo(randint(0, x), randint(0, y))