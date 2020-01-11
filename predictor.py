import sys
import keras
import keras.backend as K
import numpy as np
from PIL import Image

def predict():
    #load model
    model = keras.models.load_model("/home/ThePhilosopher/image-supersizer/models/model.h5")

    # get filename from the bash command
    filename = sys.argv[1]

    # fetch image
    image = Image.open("/home/ThePhilosopher/image-supersizer/uploads/" + filename)
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
    prediction.save("/home/ThePhilosopher/image-supersizer/predictions/" + filename)

    # delete variables to save memory
    del image, prediction, model, filename

if __name__ == "__main__":
    predict()
