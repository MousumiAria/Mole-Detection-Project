
from flask import Flask, jsonify, request, render_template, redirect
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow import keras
import os
import numpy as np


app = Flask(__name__)
uploads_dir = "/home/becode/BeCode Projects/Mole-Detection-Project/images"


@app.route("/upload-image/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            req_image = request.files["image"]

            req_image.save(os.path.join(uploads_dir, req_image.name))

            # Load your image. Make sure it is loaded in with the right dimensions for your model!
            image_size = (224, 224)
            original_image = image.load_img(os.path.join(uploads_dir, req_image.name), target_size=image_size)

            # Convert your image pixels to a numpy array of values .
            image_array = image.img_to_array(original_image)

            # Reshape your image dimensions so that the colour channels correspond to what your model expects.
            image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))

            # Preprocess your image with preprocess_input.
            prepared_image = preprocess_input(image_array)
                                
            # Loading model to compare the results
            model = keras.models.load_model('/home/becode/BeCode Projects/Mole-Detection-Project/Model')                    
            
            # Predict the class of your picture.
            prediction = model.predict(prepared_image)           
            final_prediction=prediction.max()            
            final_mole_id=np.where(prediction [0]== final_prediction)
            x= final_mole_id[0][0]    
            dict = {0: 'Actinic keratoses (akiec)',
                    1: 'Basal cell carcinoma (bcc)',
                    2: 'Benign keratosis-like lesions (bkl)',
                    3: 'Dermatofibroma (df)',
                    4: 'Melanoma (mel)',
                    5: 'Melanocytic nevi (nv)',
                    6: 'Vascular lesions (vasc)'}

            predicted_mole_name=dict[x]         
            
            return  render_template('Upload_Image.html',Mole_Image = predicted_mole_name, result = 1)

    else:
        return render_template("Upload_Image.html")


app.run(host='localhost', port=5002)
#app.run()
