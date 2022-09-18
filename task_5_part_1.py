#1

class StringVar:

	def __init__(self):
		self.text = ''

	def set(self, text):
		self.text = text

	def get(self):
		return self.text

	def prnt(text):
		print(text.set('////////'))
		print(text.get())

text = StringVar()
text.prnt()



#2

'''x = int(input("x = "))
y = int(input("y = "))

import matplotlib.pyplot as plt

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist(self):
		plt.plot([x],[y], 'ro')
		plt.show()

d = Point(x, y)
d.dist()'''
