# importing pandas as pd
import pandas as pd

def predictedTweets(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
            df = pd.read_csv(f)
    # Get Values for Prediction Results
    print(df.columns.values)
    cols = ["username", "tweet"]
    df_small = df[cols]
    df_small = df[df['label'] == 1]

    # Misinformation Dict for Data
    prediction_data = {}
    prediction_data.tweets = df.shape[0]
    prediction_data.misinfo = df_small.shape[0]
    prediction_data.handle = df["username"][0]
    

    return prediction_data, df_small