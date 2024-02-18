from fastapi import FastAPI, File, UploadFile
import numpy as np
import tensorflow as tf
from PIL import Image
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, "trained_model")

model = tf.keras.models.load_model(model_path)
CLASS_NAMES = ["Early Blight", "Late Blight",  "Healthy"]

app = FastAPI()

@app.post("/")
def predict(file: UploadFile):
    image = Image.open(file.file)
    image = image.resize((256, 256))
    image_array = np.expand_dims(np.array(image), 0)

    # Perform prediction using the loaded model
    try:
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions[0])

        # Display the prediction result
        result_text = f"{CLASS_NAMES[predicted_class]}"
    except:
        result_text = "Unknown"

    return {"prediction": result_text}