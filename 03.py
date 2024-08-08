import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


header = ['preg', 'plas', 'pres', 'skin',
          'test', 'mass', 'pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)

array = data.values


X= array[:, 0:0]
Y= array[:, 8]
print(X.shape, Y.shape)

scaler = Binarizer(threshold=0.5)
rescaled_X = scaler.fit_transform(X)
print(rescaled_X)
