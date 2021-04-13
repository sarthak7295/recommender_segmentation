from flask import Flask, flash, redirect, render_template, request, url_for
import numpy as np
import helper
from itertools import dropwhile
import pandas as pd
from sklearn.preprocessing import LabelEncoder


path_prod ='./product.csv'
df_prod = pd.read_csv(path_prod, sep=',')
app = Flask(__name__)




@app.route('/s')
def index():
    return render_template('new_home.html', data=[{'name': 'Mnist'}, {'name': 'ImageNet'}])


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/recommend/', methods=['POST'])
def predict():
    model, prod_db = helper.init_model()
    data = request.get_json()
    print(data['name'])
    user = np.array([1, 2, 3, 4, 4])
    user_t = np.array([user for i in range(len(prod_db))])
    predictions = model.predict([user_t, prod_db])
    predictions = np.array([a[0] for a in predictions])
    pred = predictions.tolist()
    list_string = map(str, prod_db)
    sorted_list = pred.copy()
    sorted_list.sort()
    threshold = sorted_list[-6]
    response = dict(zip(list_string, pred))
    res = {}
    prod_id_list = []
    for key in response:
        if response[key]>threshold:
            d = df_prod.loc[df_prod['ProductId'] == int(key)]
            l = d.values.tolist()
            str1 = 'Product : ' + l[0][1] + ' ,  Product Category : ' + l[0][2]+'  '
            prod_id_list.append(str1)
            res[key] = str1 + ', Rating : ' + str(round(response[key], 2))
            # key_value is the rating here
    return res


@app.route('/get/users', methods=['GET'])
def get_users():
    res = helper.get_users()
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)

