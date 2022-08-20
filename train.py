# Here we are training the model the model with the prefered parameters (found by mlflow experiemnts)
# We use the preprocessing.py to trasnform the data
# We save the model in the mlflow destination (S3 bucket)

# Libraries
import pandas as pd

import mlflow

from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# Mlflow
# mlflow.set_tracking_uri("sqlite:///mlflow.db")
# mlflow.set_experiment("testing-mlflow")

# dont forget to create a bucket and set it here: #TODO: make a variables file for these global parameters
# mlflow.create_experiment("semicon-sensor-clf12","s3://mlflow-semicon-clf/")
# mlflow.set_experiment("semicon-sensor-clf12")

# prefect
from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

# Data
@task
def read_data(file_path='.\\data\\uci-secom.csv'):

    df = pd.read_csv(file_path, delimiter=',')
    df = df.drop("Unnamed: 0", axis=1, inplace=False, errors='ignore')
    return df


# preprocess
@task
def preprocess_semicon(df: object):
    """
    This preporcess function gets the input semicon data as a pandas dataframe type and returns the
    scaler trasnformation, PCA transformation and the splited train and test dataframes.
    """

    # 1) under sample data

    # class count
    class_count_0, class_count_1 = df['Pass/Fail'].value_counts()

    # Separate class
    class_0 = df[df['Pass/Fail'] == -1]
    class_1 = df[df['Pass/Fail'] == 1]  # print the shape of the class
    print('class 0:', class_0.shape)
    print('class 1:', class_1.shape)

    class_0_under = class_0.sample(class_count_1 * 4)

    test_under = pd.concat([class_0_under, class_1], axis=0)

    print("total class of 1 and 0:", test_under['Pass/Fail'].value_counts())

    X = test_under.drop(['Pass/Fail', 'Time'], axis=1)
    y = test_under['Pass/Fail']

    le = LabelEncoder()
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.15
    )

    return X_train, X_test, y_train, y_test


# train and test
@task
def model_train(X_train, X_test, y_train, y_test):
    with mlflow.start_run():

        params = {"n_neighbors": 3, "Imputer_strategy": 'median', "PCA_components": 15}

        pipeline = make_pipeline(
            SimpleImputer(strategy='median'),
            StandardScaler(),
            PCA(n_components=15),
            KNeighborsClassifier(n_neighbors=3),
        )

        pipeline.fit(X_train, y_train)

        # test
        y_pred = pipeline.predict(X_test)

        # compute accuracy of the model
        score = pipeline.score(X_test, y_test)
        print(score)

        # mlflow
        mlflow.set_tag("Data Scientist", "Astellas")
        mlflow.log_params(params)
        mlflow.sklearn.log_model(pipeline, "artifacts")
        mlflow.log_metric("score", score)

    return score, y_test, y_pred


@flow(task_runner=SequentialTaskRunner())
def main(file_path: str = '.\\data\\uci-secom.csv'):

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    # mlflow.set_experiment("testing-mlflow")

    # dont forget to create a bucket and set it here: #TODO: make a variables file for these global parameters
    mlflow.create_experiment("semicon-sensor-clf15", "s3://mlflow-semicon-clf/")
    mlflow.set_experiment("semicon-sensor-clf15")

    df = read_data(file_path)
    X_train, X_test, y_train, y_test = preprocess_semicon(df).result()
    score, y_test, y_pred = model_train(X_train, X_test, y_train, y_test).result()

    # print confusion matrix
    print(classification_report(y_test, y_pred))


main()
