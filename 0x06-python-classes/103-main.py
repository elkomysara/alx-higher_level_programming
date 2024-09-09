#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

magic = MagicClass(5)
print("Radius:", magic._MagicClass__radius)
print("Area:", magic.area())
print("Circumference:", magic.circumference())
