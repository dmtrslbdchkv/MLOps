import pandas as pd
import sys


def clean(input_path, output_path):
    pre_df = pd.read_csv(input_path)
    new_df = pre_df.drop('price', axis=1)
    new_df.to_csv(output_path, index=False)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python transform.py <input_path> <output_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean(input_file, output_file)
