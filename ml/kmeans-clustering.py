from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = datasets.load_iris()

X = iris.data
Y = iris.target
labels = pd.DataFrame(Y)
labels.columns = ['label']
data = pd.DataFrame(X)
data.columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']

model = KMeans(n_clusters=3, algorithm='auto')
model.fit(X)
predict = pd.DataFrame(model.predict(X))
predict.columns = ['predict']

df = pd.concat([labels, predict], axis=1)
print(df)

ct = pd.crosstab(df['label'], df['predict'])
print(ct)