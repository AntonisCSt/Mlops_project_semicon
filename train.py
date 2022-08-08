# Here we are training the model the model with the prefered parameters (found by mlflow experiemnts)
# We use the preprocessing.py to trasnform the data
# We save the model in the mlflow destination (S3 bucket)

# Libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import mlflow
from preprocessing import preprocess_semicon
from sklearn.metrics import classification_report

#Mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
#mlflow.set_experiment("testing-mlflow")

#dont forget to create a bucket and set it here: #TODO: make a variables file for these global parameters
mlflow.create_experiment("semicon-sensor-clf","s3://mlflow-semicon-clf/")
mlflow.set_experiment("semicon-sensor-clf")

# Data 
df = pd.read_csv('.\\data\\uci-secom.csv',delimiter=',')
df = df.drop("Unnamed: 0", axis=1, inplace=False)

# preprocess
X_train, X_test, y_train, y_test, sc, pca_tr = preprocess_semicon(df)

# train and test
with mlflow.start_run():

    params = {"n_neighbors": 3}
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # test
    y_pred = knn.predict(X_test)

    # compute accuracy of the model
    score = knn.score(X_test, y_test)
    print(score)

    # mlflow
    mlflow.set_tag("Data Scientist","Astellas")
    mlflow.log_params(params)
    mlflow.sklearn.log_model(knn,"artifacts")
    mlflow.log_metric("score", score)


# print confusion matrix
print(classification_report(y_test, y_pred))