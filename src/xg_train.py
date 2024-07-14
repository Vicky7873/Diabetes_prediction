# import xgboost
from xgboost import XGBClassifier
import pandas as pd
import os
import yaml
import argparse
import numpy as np
from get_data import read_params
from split_data import split_data
import pickle
from ANN_train import get_metrics


def model_xg_train(config_path):
    config = read_params(config_path)
    learning_rate = config["XGB"]["learning_rate"]
    n_estimators = config["XGB"]["n_estimators"]
    max_depth = config["XGB"]["max_depth"]

    xg_cls = XGBClassifier(learning_rate= learning_rate, max_depth= max_depth, n_estimators= n_estimators)
    X_train,X_test,y_train,y_test = split_data(config_path)

    X_train_transform_path = config["transform_data"]["X_train_transform"]
    X_test_transform_path = config["transform_data"]["X_test_transform"]

    X_train_transform = pd.read_csv(X_train_transform_path)
    X_train_transform.head(2)
    print("========= for X_train_transform =========")
    X_test_transform = pd.read_csv(X_test_transform_path)
    X_test_transform.head(2)
    print("========= for X_test_transform =========")

    xg_cls.fit(X_train_transform,y_train)
    save_model_path = config["model_save1"]["model_dir1"]
    pickle.dump(xg_cls, open(save_model_path,'wb'))

    xg_pred = xg_cls.predict(X_test_transform)

    acc_score,classification_rep,roc_auc = get_metrics(y_test,xg_pred)
    print(f"model have {acc_score}% accuracy score")
    print(classification_rep)
    print(f"model have {roc_auc}% roc_auc score")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    model_xg_train(config_path=parsed_args.config)




