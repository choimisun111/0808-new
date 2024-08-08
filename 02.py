import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

header = ['preg', 'plas', 'pres', 'skin',
          'test', 'mass', 'pedi','age','class']

data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)
plt.clf()
#data.hist(figsize=(12,10), bins=5)
#plt.tight_layout
#plt.savefig("./result/histogram.png")
data.plot(kind='density',figsize=(12,10), subplots= True, layout=(3,3), sharex=False)
pd.plotting.scatter_matrix(data)
plt.savefig("./result/scatter.png")