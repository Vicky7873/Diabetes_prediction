# create env
 conda create -n env_name python=3.12 -y

 # 2. git initialization done
 echo "# Diabetes_prediction" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Vicky7873/Diabetes_prediction.git
git push -u origin main

# create temp.py to create folders and files
# dvc init
# dvc add dataset/kaggle_diabetes.csv
# dvc remote add -d storage gdrive://1KI0Y7QQbUfqC4o0nKizJHvMx2mBo9rH7
# dvc push

# when we want to pull the data set
# touch cmd to create files in folder using terminal -> touch src/get_data.py
# mv get_data.py src -> move file from one to another folder
# 