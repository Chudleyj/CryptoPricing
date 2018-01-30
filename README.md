# CryptoPricing
Live crypto currency pricing from CoinMarketCap, easily add your preferred coins to the code. Refreshes prices every second

TO USE:

Must have node.js installed

Then run:
$ npm install coinmarketcap
# OR 
$ yarn add coinmarketcap

Then, in terminal:
node CryptoPricing.js

To use graphing data and JSON file, just run the node.js program for as long as you would like to gather data for, then run the python program to produce graph of the data.

NOTE: 
With the latest version the JSON file posted earlier will NOT work anymore, this app has migrated to use postgres SQL so it can read and write to the data base at the same time allowing for self updating graphs. You will need to setup your own Postgres SQL database and point the node.js and python programs to the location of your database.
