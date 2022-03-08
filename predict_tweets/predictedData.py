# importing pandas as pd
import pandas as pd
# from IPython.display import HTML

def predictedTweets(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
            df = pd.read_csv(f)
    # Get Values for Prediction Results
    print(df.columns.values)
    df_small = df['tweet', 'username']
#     df_false = df[df['label'] == 0]

    # Misinformation Dict for Data
#     prediction_data = {}
#     prediction_data.total = df.count(axis=0)
#     prediction_data.misinfo = df_false.count(axis=0)
#     prediction_data.headers = list(df.columns)

    # Create HTML Table
    # result_true = df_true.to_html()
#     print(prediction_data)
    return df_small