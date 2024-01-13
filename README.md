# This repo contains - 
## Content Filtering Recommendation-System built on top of Flask Web Framework  --Use VSCode
## Collaborative Filtering -- Use VSCode
## SVD & ALS algorithms for Matrix Factorization  -- Use Colab
## Neural Collaborative Filtering for Hybrid Approach -- Use Colab

## Step 1 :

Create a directory on your local machine and  download the below 2 files from the google drive link below - 

https://drive.google.com/drive/folders/1m2Ame8hgrRAB6ZNQ2PcV7JRFXquhFEfP?usp=sharing

In the same directory clone my github repo by saying - 

$git clone https://github.com/saraswatnitin/IMT_RecommendationSystem

## Step2:
Open  training.py notebook in VSCode open terminal and switch to command prompt.
Then change to bin directory and say activate to activate the virtual environment 
Then install the dependencies by saying 
$!pip install -r requirements.txt 
Then  execute training.py  to generate similarity.npy file 

If successful, this should result in similarity.npy file in the same folder

## Step3:
On the Terminal in VSCode say - 
$python app.py 

If successful this will launch a flask server listening on localhost at 5000 port 


## Step 4 
Go to folder called client and launch app.html file 
Note: Only movies present in the movies.csv file will result in recommendations



