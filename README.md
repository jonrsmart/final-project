# final-project

In this project, we set out to use machine learning models to infer opprtune times to buy/sell cryptocurrencies to generate profits. The cryptocurrencies we examined were Bitcoin, Ethereum, and Dogecoin, and we did this by utilizing two models.

    The first model identifies whether a cryptocurrency falls into one of 5 categories: "Strong Buy", "Weak Buy", "Hold", "Weak Sell", or "Liquidate" at any given time. These categories were determined using 7 of the 8 parameters outlined in the Medium article: "How to Find Stocks That Will Help You Quickly Get Rich Using Python", by Rahul Raj to determine whether a stock, or in our case a cryptocurrency, is gearing up to rapidly rise in price. (The eighth metric was only relavant to traditional stock markets so it was left out of our analysis.)

    These seven paramters were:
        1. The current price is above the 150 and 200 days moving average (MA)
        2. The 150 days MA is above the 200 days MA.
        3. The 200 days MA is trending up for at least a month.
        4. The 50 day MA is above the 150 and 200 MAs.
        5. The price is above the 50 days MA.
        6. The current price is at least 30% above its 52 week low.
        7. The current price is at least within 25% of the 52 week high.

    The alphavantage API was used to procure historical pricing data for the three subject cryptocurrencies.  Using Python and the pandas library we calculated the metrics listed above for each subject cryptocurrency from the historical price data.

    The second model attempts to use the past 30 days of closing prices to predict the price of each asset into the future 10 days.  For this model, historical pricing data was pulled from cryptocompare.com.  We used the article: "Predicting Prices of Bitcoin with Machine Learning", by Marco Santos to help construct the LSTM models we created that predict our assest prices. Although we were able to produce functional models/predictions, the models have not been optimized well enough to produce predictions we are confident in.

    The Ethereum models performed better than the Bitcoin and Dogecoin models. We believe this is due to a variety of factors. Dogecoin and Bitcoin experienced high periods of volatility during the time window that our neural network was split for testing/training on while ethereum remained slightly more constant.  Due to this excess volatility, the dogecoin and bitcoin models were biased to under-predict, and this can be visualized in out future prediction plots. Obviously, this model could be fitted/tuned better, but this code provides a good basis to build from when attempting to use machine learning to preduict cryptocurrency prices.


Sources:

    Machine Learning Model:
    https://towardsdatascience.com/predicting-bitcoin-prices-with-deep-learning-438bc3cf9a6f

    Stock Parameter Information:
    https://medium.com/analytics-vidhya/super-performance-stocks-how-to-make-more-than-1-125-on-a-single-small-cap-stock-with-python-5ea3ae393791

    Data Sources:
    https://www.alphavantage.co/
    https://www.cryptocompare.com/

    CandleStick Chart:
    https://gist.github.com/JonathanJao/eeb34facf52cbd0e3b7fe4f06ddb552e
