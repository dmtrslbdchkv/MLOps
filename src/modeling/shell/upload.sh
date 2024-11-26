#!/bin/bash

poetry run python3 src/modeling/train.py --data-path data/processed/preprocessed_data.csv --params config/hyperparams.yaml