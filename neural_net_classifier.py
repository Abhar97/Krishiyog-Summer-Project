from time import time
from split import data_split

X_train,X_test,Y_train,Y_test = data_split()

from sklearn.neural_network import MLPClassifier as mlpc

t0 = time()

clf = mlpc(alpha=1e-5,hidden_layer_sizes=(5,5),random_state=1)
clf.fit(X_train,Y_train)

print("Training Time: "+str(round(time()-t0,3))+"s")

t1 = time()

pred = clf.predict(X_test)

print("Testing Time: "+str(round(time()-t1,3))+"s")

from sklearn.metrics import accuracy_score

print(accuracy_score(Y_test,pred))
