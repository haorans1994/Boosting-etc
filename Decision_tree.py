# XG_boosting
import  numpy as np
import pandas as pd
import xgboost as xgb

# dtrain = xgb.DMatrix('train.csv?format=csv&label_column=0')
# dtest = xgb.DMatrix('test.csv?format=csv&label_column=0')
data = pd.read_csv('heart.csv')
train = data[250:]
test = data[:55]
train.to_csv("train.csv")
test.to_csv("test.csv")


