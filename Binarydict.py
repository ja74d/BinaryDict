#!/usr/bin/python3.9
from module import bindic
from font import banner
string = input(str('ENTER YOUR STRING:'))
elements = []
for i in string:
    elements.append(i)
print(elements)
for x in elements:
    bindic(x)
