from sqlite3 import Row
from wordcloud import WordCloud
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import io
import urllib
import base64
import re

def word_cloud(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
        df = pd.read_csv(f)
    if df.shape[0] == 0:
        return '../static/img/404.png'
    else:
        df['content'] = df['tweet'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
        # row_count = df.shape[0]
        txt = ' '.join(df['content'])
        wc = WordCloud(width = 400, height = 200, random_state=1, background_color='black', colormap='Pastel1', collocations=False).generate(txt)
        buffer = io.BytesIO()
        wc.to_image().save(buffer, 'png')
        b64 = base64.b64encode(buffer.getvalue())
        image_64 = 'data:image/png;base64,' + urllib.parse.quote(b64)
        return image_64
        # , row_count

def row_count(csv):
    with open(csv, encoding="utf8", errors='ignore') as f:
        df = pd.read_csv(f)
    row_count = df.shape[0]
    return row_count