from time import time
from split import data_split
from data_builder import data_builder

X,Y = data_builder()

from sklearn.cluster import KMeans

clf = KMeans(n_clusters=3)

clf.fit(X)

pred = clf.labels_

count = 0
for i in range(len(X)):
    if pred[i]==0 and int(Y[i])==2:
        count = count + 1
    elif pred[i]==1 and int(Y[i])==3:
        count = count +1
    elif pred[i]==2 and int(Y[i])==1:
        count = count + 1

print(count)
print(pred)
print(Y)
