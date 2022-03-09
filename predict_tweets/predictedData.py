# importing pandas as pd
import pandas as pd

def predictedTweets(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
            df = pd.read_csv(f)
    # Get Values for Prediction Results
    print("Shape", df.shape)
    cols = ["username", "tweet", "label"]
    df_small = df[cols]
    df_small = df_small[df_small["label"] == 1]

    # Misinformation Dict for Data
    prediction_data = {}
    
    prediction_data['misinfo'] = df_small.shape[0]
    prediction_data['handle'] = df["username"][0]
    
#     print(df_small)

    return prediction_data, df_small