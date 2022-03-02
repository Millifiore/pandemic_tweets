import numpy as np
import pandas as pd
import torch
import transformers as ppb
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
warnings.filterwarnings('ignore')

# IMPORTING THE DATASET

df = pd.read_csv('rumor_data/rumordata_cleaned.csv', delimiter=',', skiprows=1, header=None, names=['label', 'content'])  # Read in the data, skipping the labels in the first row.
pos_label = df[df['label'] == 1]  # Grab the data labeled 1 and slice 500 of them
pos_label = pos_label[:500]
neg_label = df[df['label'] == 0]  # Do the same thing above for data labeled 0
neg_label = neg_label[:500]
covid_dataset = pd.concat([pos_label, neg_label]).reset_index(drop=True)  # Concat pos/neg labels and reset the index
print(covid_dataset['label'].value_counts())

# LOADING THE PRE-TRAINED BERT MODEL
model_class = ppb.DistilBertModel  # This is the BERT model we are using. DistilBERT
tokenizer_class = ppb.DistilBertTokenizer  # Tokenizer used for DistilBERT
pretrained_weights = 'distilbert-base-cased'  # The is what we are using to pretrain BERT
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)  # Load the pretrained tokenizer
model = model_class.from_pretrained(pretrained_weights) # Load the pretrained model


# PREPROCESSING THE DATA FOR DISTILBERT
def pre_proc(series, tokenizer):  # Function for preprocessing data for encoding
    tokenized = series.apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))  # Tokenizes series
    max_len = 0  # Finds the max len of the sentences
    for i in tokenized.values:
        if len(i) > max_len:
            max_len = len(i)
    padded = np.array([i + [0] * (max_len - len(i)) for i in tokenized.values])  # Pads all list to the same size
    print(np.array(padded).shape)
    attention_mask = np.where(padded != 0, 1, 0)  # Adds masking to tell it to ignore the padding
    print(attention_mask.shape)
    return padded, attention_mask


padded, attention_mask = pre_proc(covid_dataset['content'], tokenizer)  # Pre-processes the covid_dataset


#  ENCODING WITH DISTILBERT
def encode(model, attention_mask, padded): # Function that runs the bert model and encodes the data
    input_ids = torch.tensor(padded)  # Creates input ids
    attention_mask = torch.tensor(attention_mask) # Applies the attention mask

    with torch.no_grad():  # Runs the model
        last_hidden_states = model(input_ids, attention_mask=attention_mask)  # Pulls out the encoding we need

    features = last_hidden_states[0][:,0,:].numpy()  # Create features out of the encoding

    return features


features = encode(model, attention_mask, padded)  # Create features out of encode()


# LOGISTIC REGRESSION
def log_reg(features, series):  # Runs our classification model
    labels = series
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

    parameters = {'C': np.linspace(0.0001, 100, 20)}
    grid_search = GridSearchCV(LogisticRegression(), parameters)
    grid_search.fit(train_features, train_labels)

    print('Best Parameter: ', grid_search.best_params_)
    print('Best Score Using GridSearchCV: ', grid_search.best_score_)

    lr_clf = LogisticRegression(C=5.263252631578947)  # Initiates our Logistic Regression Model
    lr_clf.fit(train_features, train_labels)  # Fits our data

    print('Logistic Regression Score: ',
          lr_clf.score(test_features, test_labels))  # Prints the accuracy score of our data

    return lr_clf.fit(train_features, train_labels)


lr_clf = log_reg(features, covid_dataset["label"])  # Saves the trained model


# TWINT DATA
def twint(df):
    twint_content = df[['tweet']]  # Subsets the dataframe to only have the "tweet column"

    padded, attention_mask = pre_proc(twint_content['tweet'], tokenizer)  # Pre-processes the twint_dataframe

    features = encode(model, attention_mask, padded)  # Create features out of encode()

    return lr_clf.predict(features)


twint_df = pd.read_csv("CandaceO_TWINT.csv")
print(twint(twint_df))

