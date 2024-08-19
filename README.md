# chickenDiseaseClassification-mlproject

## Workflow
1. update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update entity
5. update configuration manager in src cdclassifer config 
6. update the components 
7. update the pipeline
8. update main.py
9. update dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/eyash24/chickenDiseaseClassification-mlproject.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag





# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 


## Running Tensorboard 
Run the below command in terminal to view Tensorboard
```bash
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
```
If Tensorboard is throwing an error, create a new environment and install tensorflow. After that run the above command


## Macbook Specific Library Installment
Install keras-nightly for smooth running of the application
Run the below command in Terminal
```bash
pip install keras-nightly
```