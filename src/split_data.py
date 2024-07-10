import yaml
import os 
import argparse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params,get_data_set


def split_data(config_path):
    config = read_params(config_path)
    
    dataset_path = config["load_data"]["dataset"]
    X_train_path = config["split_data"]["train_path_X"]
    X_test_path = config["split_data"]["test_path_X"]
    y_train_path = config["split_data"]["train_path_y"]
    y_tet_path = config["split_data"]["test_path_y"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(dataset_path, sep=",")
    X = df.drop(columns="Outcome", axis=1)
    y = df["Outcome"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=split_ratio,random_state=random_state)

    X_train.to_csv(X_train_path,sep=",",index=False,header=True)
    X_test.to_csv(X_test_path,sep=",",index=False,header=True)
    y_train.to_csv(y_train_path,sep=",",index=False,header=True)
    y_test.to_csv(y_tet_path,sep=",",index=False,header=True)

    return X_train,X_test,y_train,y_test

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)