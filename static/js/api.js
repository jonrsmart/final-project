// Calling the API for most recent crypto Data

function get_bitcoin_data(){
    var endpoint = "https://min-api.cryptocompare.com/data/histoday";
    var url = endpoint+'?fsym=BTC&tsym=USD&limit=1';
    d3.json(url).then(function(data) {
        var time = data.Data.time
        var high = data.Data.high
        var low = data.Data.low
        var open = data.Data.open
        var close = data.Data.close
        var volume = (data.Data.volumeto - data.Data.volumefrom)
        var data_list = [time, high, low, open, close, volume];
        console.log(data_list);
    });
};
get_bitcoin_data();
