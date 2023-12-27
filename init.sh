#!/bin/bash


#prepare files for libs
echo "Preparing libs folder"
mkdir -p libs

# load libs
echo "loading libs"
git clone -b main https://rabindra-neupane-legoai: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@github.com/LEGOAI-TECHNOLOGIES/smart_query.git libs/smart_query

git clone -b master https://rabindra-neupane-legoai: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@github.com/LEGOAI-TECHNOLOGIES/DQ.git libs/dq

git clone -b main https://rabindra-neupane-legoai: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@github.com/LEGOAI-TECHNOLOGIES/fqe.git libs/fqe


#remove all .git files of libs
echo "removing .git directories from libs"
find ./libs -type d -name ".git" -exec rm -rf {} +

echo "setting up env"
#python -m venv env
#source env/bin/activate
pip install -r requirements.txt

echo "Running app..."
python run.py
