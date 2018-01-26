import ijson
import matplotlib.pylab as plt
import numpy as np

def getMax(n):
    temp = 0
    for x in range (0,len(n)):
        if(n[x] > temp):
            temp = n[x]
    return temp


def getMin(n):
    temp = n[0]
    for x in range(0,len(n)):
        if(n[x]< temp):
            temp = n[x]
    return temp

filename = "Data.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'BitCoin.item')
    columns = list(objects)
    length = len(columns)
    prices = []
    ax = []
    temp = 0

    for x in range (0, len(columns)):
        temp = columns[x]
        prices.append(temp[u'price'])
        ax.append(x)

maxVal = float(getMax(prices))
minVal = float(getMin(prices))

plt.plot(ax, prices)
plt.axis(xmin = 0, xmax = len(prices),ymin = minVal, ymax = maxVal)
plt.show()
