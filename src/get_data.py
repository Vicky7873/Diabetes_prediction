# import pandas as pd
# import os
# import yaml
# import argparse


# def read_params(config_path):
#     with open(config_path) as yaml_file:
#         config = yaml.safe_load(yaml_file)
#         return config
    
# def get_data_set(config_path):
#     config = read_params(config_path)
#     data_path = config["data_source"]["dataset"]
#     df = pd.read_csv(data_path, sep=",")
#     print(df.head(2))
#     return df


# if __name__ == "__main__":
#     args = argparse.ArgumentParser()
#     args.add_argument("--config", default= 'params.yaml')
#     parsed_args = args.parse_args()
#     data = get_data_set(config_path=parsed_args.config)


import pandas as pd
import os
import yaml
import argparse
from typing import Union

def read_params(config_path: Union[str, dict]):
    if isinstance(config_path, str):
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
    elif isinstance(config_path, dict):
        config = config_path
    else:
        raise ValueError("Invalid config_path type. Expected str or dict.")
    
    return config
    
def get_data_set(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["dataset"]
    df = pd.read_csv(data_path, sep=",")
    print(df.head(2))
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default='params.yaml')
    parsed_args = args.parse_args()
    data = get_data_set(config_path=parsed_args.config)