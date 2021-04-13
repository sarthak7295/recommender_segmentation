import pandas as pd
import json
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


client_enc = LabelEncoder()
prod_enc = LabelEncoder()
prod_cat_enc = LabelEncoder()
prod_id_enc = LabelEncoder()


df_client_rfm = pd.read_csv('./client_rfm.csv', sep=',')
df_client_rfm = df_client_rfm[['Client','Rank_Recency','Rank_Frequency','Rank_Monetary','Cluster']]
df_client_rfm.drop_duplicates(keep='first',inplace=True)


def get_users():
    result = df_client_rfm.to_json(orient='records')
    return result


def init_model():
    df = pd.read_csv('./dataset_brazil.csv', sep=',')
    # df_client_rfm = pd.read_csv('./client_rfm.csv', sep=',')
    # df_client_rfm = df_client_rfm[['Client','Rank_Recency','Rank_Frequency','Rank_Monetary','Cluster']]
    
    model_rfm = keras.models.load_model('./regression_model.h5')
    
    df_product = df[['ProductId','Product','Product Category','Product Cost']].copy()
    df_product.drop_duplicates(keep='first',inplace=True) 
    
    df_product['Product'] = prod_enc.fit_transform(df_product['Product'].values)
    df_product['Product Category'] = prod_cat_enc.fit_transform(df_product['Product Category'].values)
    df_product['ProductId'] = prod_id_enc.fit_transform(df_product['ProductId'].values)
    product_db = np.array(list(set(df_product['ProductId'])))
    return model_rfm, product_db
