import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # load_model
        model = tf.keras.models.load_model(os.path.join('artifacts_V1', 'training', 'model.h5'))

        imagename = self.filename
        test_image = tf.keras.preprocessing.image.load_img(imagename, target_size=(224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # classes = ['Salmonella', 'Coccidiosis', 'New Castle Disease', 'Healthy']