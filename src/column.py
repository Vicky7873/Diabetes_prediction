from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pickle
import argparse

# Assuming 'X' and 'y' are already defined
# Define the steps of the pipeline
def pipe(X):
    pipeline = Pipeline(steps=[
    ('scaler', StandardScaler())  # StandardScaler is used as an example step
                                ])

    p2 = ColumnTransformer([('cols',pipeline,X.columns)])
    pickle.dump(p2,open("/Users/bhikipallai/Desktop/Projects/Machine_Learning_Projects/saved_models/p2.pkl","wb"))

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    print("done")
