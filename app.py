from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cdclassifier.utils.common import decodeImage
from cdclassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# app = Flask(__name__)
# CORS(app)


# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#         self.classifier = PredictionPipeline(self.filename)


# @app.route("/", methods=['GET'])
# # @cross_origin()
# def home():
#     return render_template('index.html')


# @app.route("/train", methods=['GET','POST'])
# # @cross_origin()
# def trainRoute():
#     os.system("python main.py")
#     return "Training done successfully!"



# @app.route("/predict", methods=['POST'])
# # @cross_origin()
# def predictRoute():
#     image = request.json['image']
#     decodeImage(image, clApp.filename)
#     result = clApp.classifier.predict()
#     return jsonify({"image": result})


# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host='0.0.0.0', port=8080) #local host
#     # app.run(host='0.0.0.0', port=8080) #for AWS


from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Path to save the uploaded image
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class ClientApp:
    def __init__(self):
        self.filename = "uploads/inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400
    
    image = request.files['image']
    
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the image
    image_path = os.path.join(UPLOAD_FOLDER, 'inputImage.jpg')
    image.save(image_path)
    
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(debug=True)
