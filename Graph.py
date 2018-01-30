import matplotlib.pylab as plt #Graphing
import matplotlib.animation as animation #Self updating Graphs
import psycopg2 as p #Postgres SQL

fig = plt.figure()
st = fig.suptitle("Crypto Currency Prices", fontsize = "large") #Graph window title

ax1 = fig.add_subplot(212) #Bitcoin
ax2 = fig.add_subplot(221) #Ripple
ax3 = fig.add_subplot(222) #Stellar

#Self Updating graph loop
def animate(i):

    #Change dbname, user, host, and password to your personal answers for each :)
    try:
        conn = p.connect("dbname= 'database' user= 'justin_chudley' host= 'localhost' password= 'password'")
    except:
        print "Database connection failed!"

    cur = conn.cursor()
    cur.execute("""SELECT * from cryptos """) #Get ALL data from database
    rows = cur.fetchall() #Save ALL data from database to rows

    ID = [] #ID value in database, new ID is created every second, therefore this can track seconds elapsed
    BTC = [] #Bitcoin
    RIP = [] #Ripple
    STEL = [] #Stellar


    for x in range(0, len(rows)):
        ID.append(rows[x][0]) #Get ID column data isolated
        BTC.append(rows[x][1]) #Get Bitcoin column data isolated
        RIP.append(rows[x][2]) #Get Ripple column data isolated
        STEL.append(rows[x][3]) #Get Stellar column data isolated

    #Must clear old graph data every second for new updated graphs
    ax1.clear()
    ax2.clear()
    ax3.clear()

    #Titels of each subgraph
    ax1.set_title('Bitcoin')
    ax2.set_title('Ripple')
    ax3.set_title('Stellar')

    #Labels for graph axis
    ax1.set_xlabel('Seconds Elapsed')
    ax1.set_ylabel('Price (USD)')

    #Labels for graph axis
    ax2.set_xlabel('Seconds Elapsed')
    ax2.set_ylabel('Price (USD)')

    #Labels for graph axis
    ax3.set_xlabel('Seconds Elapsed')
    ax3.set_ylabel('Price (USD)')

    #Plot each subgraph
    ax1.plot(ID, BTC)
    ax2.plot(ID,RIP)
    ax3.plot(ID,STEL)

#Fit to window without overlaps
fig.set_tight_layout(True)

#Update graph with animate function, inveral = 1000 means every 1 second
ani = animation.FuncAnimation(fig, animate, interval = 1000)

#Draw the graph to the window
plt.show()
