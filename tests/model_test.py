from pathlib import Path
import train


# In Prefect, to test an individual task, you can access the original function using .fn
def test_read_data_task():
    # this needs to be tested with the users input data

    test_path = Path(".\\tests\\train_test.csv")
    df = train.read_data.fn(file_path=test_path)

    assert len(df.columns)==592

def test_preprocess_data_task():
    

    test_path = Path(".\\tests\\train_test.csv")
    df = train.read_data.fn(file_path=test_path)

    X_train, X_test, y_train, y_test = train.preprocess_semicon.fn(df)

    assert len(X_train.columns)==590
    assert len(X_test.columns)==590
