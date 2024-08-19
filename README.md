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

## Running Tensorboard 
Run the below command in terminal to view Tensorboard
`tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/`
If Tensorboard is throwing an error, create a new environment and install tensorflow. After that run the above command


## pip install keras-nighlty

## DVC
Run the following after cloning the repository
```
dvc init
dvc repro
```

The below command will return a DAG of dependency graph between all the stages of the pipeline
`dvc dag`