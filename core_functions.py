import keras
import numpy as np
from PIL import Image

class Predictor():

	def __init__(self):
		self.model = keras.models.load_model("./models/model.h5")

	def predict(self, filename):
		image = self.get_prediction(filename)
		image[image > 255] = 255
		image[image < 0] = 0
		image = Image.fromarray(image.astype(np.uint8))
		image.save('./predictions/' + filename)
		del image 	# delete image to save memory

	def get_prediction(self, filename):
		image = self.fetch_image(filename)
		prediction = self.model.predict(np.array([image]))
		image_hr = prediction[0] * 255
		del image, prediction 	# delete variables to save memory
		return image_hr

	def fetch_image(self, filename):
		# Todo: implement
		image = Image.open('./uploads/' + filename)
		image = np.array(image)
		image = image.astype('float32') / 255
		return image