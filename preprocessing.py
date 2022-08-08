# Here we preprocess the raw data we get for the semicon input data.
# This script will be used in the training.py and the inference.py (also in test.py)

# Libraries
import pandas as pd

# Modeling libraries
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

def preprocess_semicon(df:object):
    """
    This preporcess function gets the input semicon data as a pandas dataframe type and returns the
    scaler trasnformation, PCA transformation and the splited train and test dataframes.
    """

    # 1) under sample data

    # class count
    class_count_0, class_count_1 = df['Pass/Fail'].value_counts()

    # Separate class
    class_0 = df[df['Pass/Fail'] == -1]
    class_1 = df[df['Pass/Fail'] == 1]# print the shape of the class
    print('class 0:', class_0.shape)
    print('class 1:', class_1.shape)

    class_0_under = class_0.sample(class_count_1*4)

    test_under = pd.concat([class_0_under, class_1], axis=0)

    print("total class of 1 and 0:",test_under['Pass/Fail'].value_counts())# plot the count after under-sampeling
    test_under['Pass/Fail'].value_counts().plot(kind='bar', title='count (target)')


    # 2) split data

    #without reduced data
    #X = df.drop(['Pass/Fail','Time'], axis=1)
    #y = df['Pass/Fail']

    #with reduced data
    #first reduce data positives
    X = test_under.drop(['Pass/Fail','Time'], axis=1)
    y = test_under['Pass/Fail']

    le = LabelEncoder()
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        stratify=y, 
                                                        test_size=0.15)



    # 3) cleaning method mean


    imp_mean = SimpleImputer( strategy='median') #for median imputation replace 'mean' with 'median'
    imp_mean.fit(X_train) #need to save this for later

    #transform data  (fill nans)
    X_train = imp_mean.transform(X_train)
    X_test = imp_mean.transform(X_test)



    # 4) scale data

    # Standardizing the features
    sc = StandardScaler().fit(X_train)

    #transform data  (scale data)
    X_train = sc.transform(X_train)
    X_test = sc.transform(X_test)


    # 5) Use PCA

    pca = PCA(n_components=15)
    pca_tr = pca.fit(X_train)

    #transform data  (PCA)
    X_train = pca_tr.transform(X_train)
    X_test = pca_tr.transform(X_test)

    X_train = pd.DataFrame(data = X_train)
    X_test = pd.DataFrame(data = X_test)



    return X_train, X_test, y_train, y_test, sc, pca_tr