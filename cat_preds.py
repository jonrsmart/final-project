import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import TimeSeriesSplit
from tensorflow.keras.models import load_model

def buy_or_sell(coin):
    df = pd.read_csv(f'static/updated_csv/{coin}_current.csv')
    df.sort_values(by=['Date'], inplace=True, ascending=True)
    X_test = df.iloc[-5:]
    X_test.reset_index(inplace=True)
    X_test.drop(['Date', 'index'], axis=1, inplace=True)
    X_scaler = MinMaxScaler()
    X_test_scaled = X_scaler.fit_transform(X_test)
    model = load_model(f"static/models/{coin}_squential.h5")
    test = np.array([X_test_scaled[-1]])
    predictions = model.predict(test)
    classes = np.argmax(predictions, axis=1)
    label_names = pd.DataFrame([[0,"Buy"],[1, "Hold"], [2, "Weak Sell"], [3, "Strong Buy"],[4,"Liquidate"]], columns = ["Value", "Label"])
    output = label_names['Label'].loc[classes].to_string()
    return output
    