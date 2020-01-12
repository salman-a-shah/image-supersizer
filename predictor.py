"""
This script loads the model and the user uploaded image, makes a
prediction, then saves the prediction in hard disk. This script is
run every time a user requests an image to be supersized.

The system is implemented this way to bypass a conflict with
tensorflow making predictions within flask on the servers hosted
by pythonanywhere.com.
"""
import sys
import os 
import keras
import keras.backend as K
import numpy as np
from PIL import Image
import load_environment_variables

WORKING_DIRECTORY = os.environ.get("WORKING_DIRECTORY")

def predict():
    #load model
    model = keras.models.load_model(WORKING_DIRECTORY + "models/model.h5")

    # get filename from the bash command
    filename = sys.argv[1]

    # fetch image
    image = Image.open(WORKING_DIRECTORY + "uploads/" + filename)
    image = image.convert("RGB")
    image = np.asarray(image, dtype=np.float32) / 255
    image = image[:, :, :3]

    # run model
    prediction = model.predict(np.array([image]))[0] * 255
    K.clear_session()

    # clip image
    prediction[prediction > 255] = 255
    prediction[prediction < 0] = 0

    # save image to disk
    prediction = Image.fromarray(prediction.astype(np.uint8))
    prediction.save(WORKING_DIRECTORY + "predictions/" + filename)

    # delete variables to save memory
    del image, prediction, model, filename

if __name__ == "__main__":
    predict()
