var CoinMarketCap = require ("node-coinmarketcap"); //CoinMarketCap API
var Sequelize = require("sequelize"); //Sequelize API

//Change database, justin_chudley, and password to your personal cases for each.
//Do the same for localhost.
var connection = new Sequelize('database', 'justin_chudley', 'password', { //Connect to DB
  host: 'localhost',
  dialect: 'postgres',
  logging: false,
  operatorsAliases: false
});

//Create Table and rows if not created yet
var Cryptos = connection.define('cryptos', {
  Bitcoin: Sequelize.FLOAT,
  Ripple: Sequelize.FLOAT,
  Stellar: Sequelize.FLOAT
});

var options = {
  events: true,
  refresh: 1, //Refresh data (coinmarketcap.on) every 1 second
  convert: "USD"
}

var coinmarketcap = new CoinMarketCap(options);
var BTC;
var RIP;
var STEL;

//Get BTC price
coinmarketcap.on("BTC", (coin) => {
  BTC = coin.price_usd;
});

//Get ripple price
coinmarketcap.on("ripple", (coin) => {
  RIP = coin.price_usd;
//  console.log(coin)
});

//Get Stellar price, output all 3 to console
coinmarketcap.on("stellar", (coin) => {
  STEL = coin.price_usd;
  console.log("\n ................................................\n",
  "Stellar:", STEL, " BTC:", BTC, " Ripple:", RIP);
  updateDB(); //Send prices to database update function
});

//Send prices to database
function updateDB(){
  connection.sync().then(function (){
    Cryptos.create({
      Bitcoin: BTC,
      Ripple: RIP,
      Stellar: STEL
    });
  });
}
