'''
    Python Twitter API Sentiment Analysis by Eanna Curran
    Program which plots sentiment from Twitter API

'''


import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("fivethirtyeight")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	pullData = open("TwitterAverageSentiment.csv","r").read()
	lines = pullData.split('\n')

	xar = []
	yar = []

	x = 0
	y = 0

	for l in lines:
		print(l)
		x += 1
		y = l

		xar.append(x)
		yar.append(y)

	ax1.clear()
	ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval = 1000)

plt.show()	
