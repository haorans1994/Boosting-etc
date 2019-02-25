# XG_boosting
import  numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score

import graphviz
import matplotlib
import matplotlib.pyplot as plt


# dtrain = xgb.DMatrix('train.csv?format=csv&label_column=0')
# dtest = xgb.DMatrix('test.csv?format=csv&label_column=0')
data = pd.read_csv('heart.csv')
train = data[50:]
test = data[:50]
# train.to_csv("train.csv")
# test.to_csv("test.csv")
# train = pd.read_csv('test.csv')
# test = pd.read_csv('train.csv')
# print(test)
# print(data[:250])
# divide label out of original dataset
label = train['target']
test_label = test['target']

# separate the feature data from the original dataset
train_data = train.drop(columns=['target'], inplace=False)
test_data = test.drop(columns=['target'], inplace=False)

# create DMatrix data that can be used in xboosting
dtrain = xgb.DMatrix(train_data, label=label)
dtest = xgb.DMatrix(test_data, label=test_label)

image_x = []
image_y = []

for i in range(100):
    eta = i/100
    image_x.append(eta)
# set up parameters
    param = {'max_depth': 10, 'eta': eta, 'silent': 1, 'objective': 'binary:logistic'}
    num_round = 10
    bst = xgb.train(param, dtrain, num_round)
    train_preds = bst.predict(dtrain)
# print(train_preds)
    test_predict = bst.predict(dtest)
# print(test_predict)
    predictions = [round(value) for value in test_predict]
    y_test = dtest.get_label()
    test_accuracy = accuracy_score(y_test, predictions)
    # print("Test Accuracy: %.2f%%" % (test_accuracy * 100.0))
    image_y.append(test_accuracy * 100.0)
# xgb.plot_tree(bst, num_trees=0, rankdir= 'LR' )
# pyplot.show()
plt.plot(image_x,image_y,color='red',label = 'accuracy with the eta value')


# plt.plot(stock1['date'], stock1['close'])
# plt.plot(stock2['date'],stock2['close'])
plt.xticks(rotation=30)
plt.xlabel('eta value')
plt.legend()
plt.ylabel('accuracy')
plt.title('How the accuracy of xgboosting tree related to the eta value')

plt.show()




