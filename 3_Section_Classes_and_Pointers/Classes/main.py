

from __future__ import print_function


class Cookie:
    def __init__(self, colour):
        self.colour = colour


    def getColour(self):
        return self.colour


    def setColour(self, colour):
        self.colour = colour



cookie1 = Cookie('green')
cookie2 = Cookie('yellow')

print(cookie1.getColour())
print(cookie2.getColour())


cookie2.setColour('white')

print(cookie2.getColour())
