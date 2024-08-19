from urllib.parse import urlparse
import pandas as pd
import tensorflow as tf
from pathlib import Path
from cdclassifier.config.configuration import EvaluationConfig
from cdclassifier.utils.common import save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):
        df = pd.read_csv(self.config.training_dataframe_path)

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_dataframe(
            dataframe=df,
            directory=self.config.training_data,
            x_col='images',
            y_col="label",
            subset="validation",
            seed=42,
            shuffle=True,
            class_mode="categorical",
            classes=['Salmonella', 'Coccidiosis', 'New Castle Disease', 'Healthy'],
            **dataflow_kwargs
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)