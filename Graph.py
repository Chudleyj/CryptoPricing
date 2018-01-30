import matplotlib.pylab as plt
import matplotlib.animation as animation
import numpy as np
import psycopg2 as p

fig = plt.figure()
st = fig.suptitle("Crypto Currency Prices", fontsize = "large")

ax1 = fig.add_subplot(212)
ax2 = fig.add_subplot(221)
ax3 = fig.add_subplot(222)

def animate(i):

    try:
        conn = p.connect("dbname= 'database' user= 'justin_chudley' host= 'localhost' password= 'password'")
    except:
        print "Database connection failed!"

    cur = conn.cursor()
    cur.execute("""SELECT * from cryptos """)
    rows = cur.fetchall()

    ID = [] #ID value in database, new ID is created every second, therefore this can track seconds elapsed
    BTC = [] #Bitcoin
    RIP = [] #Ripple
    STEL = [] #Stellar


    for x in range(0, len(rows)):
        ID.append(rows[x][0])
        BTC.append(rows[x][1])
        RIP.append(rows[x][2])
        STEL.append(rows[x][3])


    ax1.clear()
    ax2.clear()
    ax3.clear()

    ax1.set_title('Bitcoin')
    ax2.set_title('Ripple')
    ax3.set_title('Stellar')

    ax1.set_xlabel('Seconds Elapsed')
    ax1.set_ylabel('Price (USD)')

    ax2.set_xlabel('Seconds Elapsed')
    ax2.set_ylabel('Price (USD)')

    ax3.set_xlabel('Seconds Elapsed')
    ax3.set_ylabel('Price (USD)')

    ax1.plot(ID, BTC)
    ax2.plot(ID,RIP)
    ax3.plot(ID,STEL)


fig.set_tight_layout(True)
ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
