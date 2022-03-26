import pandas as pd

def predictedTweets(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
            df = pd.read_csv(f)
    # Get Values for Prediction Results
    df["Tweet Content"] = df["tweet"]
    df[" "] = df["Unnamed: 0"]
    for i in df[" "]:
        df[" "][i] = df[" "][i] + 1
    print("Shape", df.shape)
    cols = [" ","Tweet Content"]
    df_small = df[cols]

    # Misinformation Dict for Data
    prediction_data = {}
    prediction_data['misinfo'] = df_small.shape[0]
    prediction_data['handle'] = df["username"][0]

    return prediction_data, df_small