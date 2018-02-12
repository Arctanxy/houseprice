from sklearn import ensemble
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
import pandas as pd 
import numpy as np 

train_data = pd.read_csv('H://kaggle/houseprice/data/Mtrain.csv')
test_data = pd.read_csv('H://kaggle/houseprice/data/Mtest.csv')

all_data = pd.concat([train_data,test_data])

useless_feature = ['Alley','PoolQC','Fence','MiscFeature']
all_data = all_data.drop(useless_feature,axis=1)
print(all_data.info())
print(all_data.describe())
