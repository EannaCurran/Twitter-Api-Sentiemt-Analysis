'''
    Python Twitter API Sentiment Analysis by Eanna Curran
    Program which plots sentiment of tweets from Twitter API

'''


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

# Function to update figures used in graph
def animate(i):
    global new

    pullData = open("TwitterAverageSentiment.csv","r").read()
    data = pullData.split('\n')

    for n in data[:-1]:
        new.append(float(n))

    plt.plot(new, 'b')
    new = []

# Setting up graph
style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
new = []

# Calling funciton to update graph
ani = animation.FuncAnimation(fig, animate, interval = 30000)
plt.show()
