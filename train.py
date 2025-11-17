
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def load_data():
    df = pd.read_csv(r"data/train.csv")
    return df


def train_model(df):
    features = [col for col in df.columns if col not in ["id", "FloodProbability"]]

    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

    y_full_train = df_full_train["FloodProbability"].values
    X_full_train = df_full_train[features].values

    model = LinearRegression()
    model.fit(X_full_train, y_full_train)

    return model


def save_model(filename, model):
    with open(filename, "wb") as f_out:
        pickle.dump(model, f_out)

    print(f"Model saved to {filename}")


df = load_data()
model = train_model(df)
save_model("model.bin", model)
