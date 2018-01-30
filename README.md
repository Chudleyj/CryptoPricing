# CryptoPricing
Live crypto currency pricing from CoinMarketCap, easily add your preferred coins to the code. Refreshes prices every second.
Node.js app takes data it is showing you and saves into postgres database.
Additonal python program takes the prices from the database and makes easy to read graphs that update themselves every second (you can run the node.js app and python app together and the graphs will keep up to date with the new data!)

TO USE:

Must have node.js installed

Then run:

$ npm install coinmarketcap
# OR 
$ yarn add coinmarketcap
# AND 
npm install sequelize

Then, in terminal:

node CryptoPricing.js

TO USE PYTHON PROGRAM:

Must have python installed

Must have pip installed (Not technically MUST have pip, you could manually install the libs needed, but not worth the time)

Then run:
$ pip install matplotlib

# AND

$ pip install psycopg2 (if you are using postgres)

Then, in terminal:

python Graph.py

NOTE: 
With the latest version the JSON file posted earlier will NOT work anymore, this app has migrated to use postgres SQL so it can read and write to the data base at the same time allowing for self updating graphs. You will need to setup your own Postgres SQL database and point the node.js and python programs to the location of your database (Comments located in node.js and python code to show you where to do this.)
