# import random
# GLOBAL_NAME=set()
# UPPERCASE='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# DIGITS='1234567890'

# def generate_name():
#     return ''.join((random.choice(UPPERCASE), random.choice(UPPERCASE), random.choice(DIGITS), random.choice(DIGITS), random.choice(DIGITS)))
# def choose_name():
#     if len(GLOBAL_NAME)==676000:
#         raise RuntimeError("Namespace is full")
#         name=genetate_name
#         while name in GLOBAL_NAME:
#             name=generate_name()
#         GLOBAL_NAME.add(name)
#         return name
# class Robot(object):
#     def __init__(self):
#         self.name= choose_name()
#     def reset(self):
#         self.__init__()
import string
import random

class Robot:
    def __init__(self):
        Robot.reset(self)
    def reset(self):
        self.name=generate_name()
def generate_name():
    random.seed()
    name=""
    for i in range(0,2):
        name+=random.choice(string.ascii_uppercase)
    for i in range(0,3):
        name+= random.choice(string.digits)
    return name    