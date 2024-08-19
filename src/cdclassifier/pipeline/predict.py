import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename=None):
        self.filename = filename
        self.model = tf.keras.models.load_model(os.path.join('artifacts_V1', 'training', 'model.h5'))
    
    def predict(self, filename_image=None):
        # load_model
        self.filename_image = filename_image
        
        if self.filename:
            imagename = self.filename
        elif filename_image:
            imagename = self.filename_image

        test_image = tf.keras.preprocessing.image.load_img(imagename, target_size=(224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        result = self.model.predict(test_image)
        result = result.tolist()
        result = result[0]

        classes = ['Salmonella', 'Coccidiosis', 'New Castle Disease', 'Healthy']
        for i,j in enumerate(classes):
            if int(result[i]) == 1:
                return {
                    "class": j,
                    "confidence": 1
                }
            
        return {
            "class": "Salmonella",
            "confidence": 0
        }
        
    
if __name__ == "__main__":
    file_list = [
            ['salmo.432.jpg','Salmonella'],
            ['salmo.466.jpg','Salmonella'],
            ['cocci.334.jpg','Coccidiosis'],
            ['ncd.213.jpg','New Castle Disease'],
            ['pcrsalmo.61.jpg','Salmonella'],
            ['salmo.1366.jpg','Salmonella'],
            ['cocci.309.jpg','Coccidiosis'],
            ['ncd.178.jpg','New Castle Disease'],
            ['cocci.738.jpg','Coccidiosis'],
            ['cocci.758.jpg','Coccidiosis'],
            ['pcrcocci.242.jpg','Coccidiosis'],
            ['pcrsalmo.35.jpg','Salmonella'],
            ['salmo.1517.jpg','Salmonella'],
            ['healthy.1555.jpg','Healthy'],
    ]
    #  artifacts/data_ingestion/Train/cocci.1.jpg

    predictpipeline = PredictionPipeline()

    for i,file in enumerate(file_list):
        print()
        file_path = os.path.join("artifacts/data_ingestion/Train",file[0])
        
        prediction = predictpipeline.predict(filename_image=file_path)
        print(prediction)

        if prediction == file[1]:
            print(f"Test case {i+1}: Pass")
        else:
            print(f"Test case {i+1}: Fail")

            