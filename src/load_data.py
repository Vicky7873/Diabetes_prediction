import os
import argparse
import get_data
from get_data import get_data_set, read_params
import yaml


def load_and_save(config_path):
    config_path = read_params(config_path)
    df = get_data_set(config_path)
    new_cols = [cols.replace(" ","_") for cols in df.columns]
    raw_data_path = config_path["load_data"]["dataset"]
    df.to_csv(raw_data_path, sep=",", index=False,header=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
