import tensorflow as tf
import pandas as pd
import keras
from cdclassifier.entity.config_entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
        self.train_generator = None
        self.valid_generator = None
        self.steps_per_epoch = None
        self.validation_steps = None

    def get_base_model(self):
        """Loads the base model from the specified path."""
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):
        """Prepares the training and validation data generators."""
        df = pd.read_csv(self.config.training_dataframe_path)

        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        # Validation data generator
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_dataframe(
            dataframe=df,
            directory=self.config.training_images_dir,
            x_col='images',
            y_col="label",
            subset="validation",
            seed=42,
            shuffle=True,
            class_mode="categorical",
            classes=['Salmonella', 'Coccidiosis', 'New Castle Disease', 'Healthy'],
            **dataflow_kwargs
        )

        # Training data generator with or without augmentation
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_dataframe(
            dataframe=df,
            directory=self.config.training_images_dir,
            x_col='images',
            y_col="label",
            subset="training",
            seed=42,
            shuffle=True,
            class_mode="categorical",
            classes=['Salmonella', 'Coccidiosis', 'New Castle Disease', 'Healthy'],
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """Saves the model to the specified path."""
        model.save(path)
        # save_object(file_path=path, obj=model)

    def train(self, callback_list: list):
        """Trains the model using the prepared generators and saves the trained model."""
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )