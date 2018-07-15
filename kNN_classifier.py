from time import time
from split import data_split

X_train,X_test,Y_train,Y_test = data_split()

from sklearn.neighbors import KNeighborsClassifier as knc

t0 = time()

clf = knc(n_neighbors = 20)
clf.fit(X_train,Y_train)

print("Training Time: "+str(round(time()-t0,3))+"s")

t1 = time()

pred = clf.predict(X_test)

print("Testing Time: "+str(round(time()-t1,3))+"s")

from sklearn.metrics import accuracy_score

print(accuracy_score(Y_test,pred))
