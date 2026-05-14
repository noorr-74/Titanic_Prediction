
import numpy as np

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def calculate_gradient(W,X,Y):
    m=Y.size#number off instances
    return (X.T @ (sigmoid(X @ W)-Y)/ m)

def gradient_descent(X,Y,alpha=0.1,num_iter=100,total=1e-7):
    b=np.c_[np.ones((X.shape[0],1)),X]
    W=np.zeros(X.shape[1])
    for i in range(num_iter):
        grad=calculate_gradient(W,X,Y)
        W -=alpha * grad
        
        if np.linalg.norm(grad)<total:
            break
    return W

def predict_proba(X,W):
        b=np.c_[np.ones((X.shape[0],1)),X]
        return sigmoid(b @ W)
def predict(X,W,threshold=0.5):
     return(predict_proba(X,W)>= threshold).astype(int)
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,y=load_breast_cancer(return_X_y=True)
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

scaler=StandardScaler()

x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

w=gradient_descent(x_train_scaled,y_train)

y_pred_train=predict(x_train_scaled,w)
y_pred_test=predict(x_test_scaled,w)

train_acc=accuracy_score(y_train,y_pred_train)
test_acc=accuracy_score(y_test,y_pred_test)

print(train_acc)
print(test_acc)





