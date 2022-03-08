import twint

def search(user_handle):
    c = twint.Config()
    c.Username = user_handle
    c.Search = "covid"
    c.Pandas = True
    twint.run.Search(c)
    tweets_df = twint.storage.panda.Tweets_df

    csv = tweets_df.to_csv()
    return csv