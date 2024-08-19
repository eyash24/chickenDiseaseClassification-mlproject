from cdclassifier.constants import *
from cdclassifier.utils.common import read_yaml, create_directories, save_json
from cdclassifier.entity.config_entity import (
    DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbacksConfig, TrainingConfig, EvaluationConfig
    )
import os
from pathlib import Path


class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            param_filepath = PARAMS_FILE_PATH
        ):
        
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url= config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            api_file=config.api_file,
            dataset=config.dataset
        ) 

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.param.IMAGE_SIZE,
            params_learning_rate = self.param.LEARNING_RATE,
            params_include_top = self.param.INCLUDE_TOP,
            params_weights = self.param.WEIGHTS,
            params_classes = self.param.CLASSES
        )
        return prepare_base_model_config

    def get_prepare_callbacks_config(self)->PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_file_path)
        create_directories([
            Path(config.tensorboard_root_log_dir),
            Path(model_ckpt_dir)
        ])

        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir= Path(config.root_dir),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir),
            checkpoint_model_file_path= Path(config.checkpoint_model_file_path)
        )

        return prepare_callbacks_config

    def get_training_config(self)->TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.param
        training_dataframe_path = os.path.join(self.config.data_ingestion.unzip_dir, "train_data.csv")
        training_images_dir = os.path.join(self.config.data_ingestion.unzip_dir, "Train")
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_dataframe_path=Path(training_dataframe_path),
            training_images_dir=Path(training_images_dir),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        
        return training_config

    def get_validation_config(self)-> EvaluationConfig:
        config = self.config.model_evaluation
        eval_config = EvaluationConfig(
            path_of_model=Path(config.trained_model_path),
            training_data=Path(config.training_data),
            all_params=self.param,
            params_image_size=self.param.IMAGE_SIZE,
            params_batch_size=self.param.BATCH_SIZE,
            training_dataframe_path=Path(config.training_dataframe_path)
        )
        return eval_config