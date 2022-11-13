from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
import numpy as np
import torch

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    file = request.files['image']
    img = Image.open(file.stream)
    img.save('output.png')
    cnn = tf.keras.models.load_model("yawn_model.h5")
    img = "output.png"

    test_image = tf.keras.utils.load_img(img, target_size = (64, 64))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    result = cnn.predict(test_image/255.0)
    print(result[0][0])
    if(result > 0.5):
        ans = "Yawn"
    else:
        ans = "No yawn"

    return jsonify({'msg': 'success', 'ans':ans, 'prob': str(result[0][0])})