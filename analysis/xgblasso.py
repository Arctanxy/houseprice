import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
def rmse(y_true,y_pred):
    return np.sqrt(mean_squared_error(y_true,y_pred))/np.mean(y_true)

train = pd.read_csv('../data/Mtrain.csv')
test = pd.read_csv('../data/Mtest.csv')

y = train.pop('SalePrice')
x = train

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.33,random_state=42
)

import xgboost as xgb

clf = xgb.XGBRegressor(
    colsample_bytree=0.2,
    gamma=0.0,
    learning_rate=0.01,
    max_depth=4,
    min_child_weight=1.5,
    n_estimators=7200,
    reg_alpha=0.9,
    reg_lambda=0.6,
    subsample=0.2,
    seed=42,
    silent=1)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print('________准确率________:%r' % rmse(y_test,y_pred))
