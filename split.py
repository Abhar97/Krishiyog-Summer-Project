from data_builder import data_builder
from sklearn.model_selection import train_test_split

def data_split():

  X,Y = data_builder()

  X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

  return X_train,X_test,Y_train,Y_test
