import yaml
import argparse
import pandas as pd
import os
import numpy as np
from get_data import read_params,get_data_set
from  standrdize_data import stc_data
from split_data import split_data
from tensorflow import keras # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import Dense,Dropout,ReLU,BatchNormalization
import pickle
from sklearn.metrics import accuracy_score,roc_auc_score,classification_report


def get_metrics(y_true,y_pred):
    acc_score = accuracy_score(y_true,y_pred)
    classification_rep = classification_report(y_true,y_pred)
    roc_auc = roc_auc_score(y_true,y_pred)
    return acc_score, classification_rep, roc_auc


def model_train(config_path):
    config = read_params(config_path)
    model = Sequential()
    kernel_initializer = config["ANN"]["kernel_initializer"]
    activation = config["ANN"]["activation"]
    input_dim = config["ANN"]["input_dim"]
    epochs = config["ANN"]["epochs"]
    batch_size = config["ANN"]["batch_size"]
    loss = config["ANN"]["loss"]
    optimizer = config["ANN"]["optimizer"]
    metrics = config["ANN"]["metrics"]
    sigmoid = config["ANN"]["sig_act"]

    model.add(Dense(units=32,kernel_initializer=kernel_initializer,activation=activation,input_dim=input_dim))
    
    model.add(Dense(units=64,kernel_initializer=kernel_initializer,activation=activation))
    model.add(Dense(units=128,kernel_initializer=kernel_initializer,activation=activation))
    model.add(Dense(units=32,kernel_initializer=kernel_initializer,activation=activation))
    model.add(Dense(units=16,kernel_initializer=kernel_initializer,activation=activation))
    model.add(Dense(units=8,kernel_initializer=kernel_initializer,activation=activation))
    model.add(Dense(units=1,kernel_initializer=kernel_initializer,activation=sigmoid))

    model.compile(optimizer=optimizer,loss=loss,metrics=[metrics])

    X_train,X_test,y_train,y_test = split_data(config_path)

    X_train_transform_path = config["transform_data"]["X_train_transform"]
    X_test_transform_path = config["transform_data"]["X_test_transform"]

    X_train_transform = pd.read_csv(X_train_transform_path)
    X_test_transform = pd.read_csv(X_test_transform_path)
    
    history = model.fit(X_train_transform,y_train,batch_size=batch_size,epochs=epochs,validation_split=0.2)
    model.summary()

    

    # model save
    model_path = config["model_save"]["model_dir"]
    pickle.dump(model, open(model_path,'wb'))


    y_pred = model.predict(X_test_transform)
    y_pred = (y_pred > 0.5)

    print(type(y_pred))
    accuracy_score, classification_rep, roc_auc = get_metrics(y_test,y_pred)
    print(f"model have {accuracy_score}% accuracy score")
    print(classification_rep)
    print(f"model have {roc_auc}% roc_auc score")

    




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    model_train(config_path=parsed_args.config)