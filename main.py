import sys 
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# if ROOT_DIR not in sys.path:
sys.path.append(ROOT_DIR)
dir_2 = os.path.join(ROOT_DIR, "src")
sys.path.append(dir_2)


from src.cdclassifier import logger
from src.cdclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cdclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cdclassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cdclassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = " Prepare Base Model Stage" 
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Training Stage"
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e
