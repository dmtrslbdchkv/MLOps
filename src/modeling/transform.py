import argparse
import pandas as pd


def preprocessing(data_path):
    df = pd.read_csv(data_path)
    new_df = df.copy()
    new_df.drop('id', axis=1, inplace=True)
    new_df.drop('title', axis=1, inplace=True)
    new_df = pd.get_dummies(new_df, columns=['genres'])
    filename = 'data/processed/preprocessed_data.csv'
    new_df.to_csv(filename, sep=',', index=False, encoding='utf-8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Преобразование датасета")
    parser.add_argument("--data-path", type=str, required=True, help="Путь до исходного датасета")
    args = parser.parse_args()
    preprocessing(args.data_path)
