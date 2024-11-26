#!/bin/bash

bash docker-compose up -d

bash poetry install

bash chmod +x src/modeling/shell/*.sh pipeline.sh preparation.sh src/shell/*.sh

bash ./src/modeling/shell/first_load.sh

bash ./src/modeling/shell/extract.sh

bash ./src/modeling/shell/preprocess.sh

bash ./src/modeling/shell/upload.sh