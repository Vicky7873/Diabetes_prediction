import yaml
import argparse
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from get_data import read_params
from split_data import split_data

def stc_data(config_path):
    config = read_params(config_path)

    X_train_transform_path = config["transform_data"]["X_train_transform"]
    X_test_transform_path = config["transform_data"]["X_test_transform"]

    X_train,X_test,y_train,y_test = split_data(config_path)
    scalar = StandardScaler()

    X_train_transform = pd.DataFrame(scalar.fit_transform(X_train), columns=X_train.columns)
    X_test_transform = pd.DataFrame(scalar.fit_transform(X_test), columns=X_test.columns)

    X_train_transform.to_csv(X_train_transform_path,index=False)
    X_test_transform.to_csv(X_test_transform_path, index=False)

    print(X_test_transform.head(2))
    print(X_train_transform.head(2))
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    stc_data(config_path=parsed_args.config)