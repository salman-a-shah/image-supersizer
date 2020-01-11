import keras
import keras.backend as K
import numpy as np
from PIL import Image

class Predictor():

	def __init__(self):
		self.model = keras.models.load_model("/home/ThePhilosopher/image-supersizer/models/model.h5")

	def predict(self, filename):
		image = self.get_prediction(filename)
		image[image > 255] = 255
		image[image < 0] = 0
		image = Image.fromarray(image.astype(np.uint8))
		image.save('/home/ThePhilosopher/image-supersizer/predictions/' + filename)
		del image 	# delete image to save memory

	def get_prediction(self, filename):
		image = self.fetch_image(filename)
		prediction = self.model.predict(np.array([image]))[0] * 255
		K.clear_session()
		del image 	# delete variables to save memory
		return prediction

	def fetch_image(self, filename):
		image = Image.open('/home/ThePhilosopher/image-supersizer/uploads/' + filename)

		# if there are 4 channels, convert to 3 channels
		# image = image[:, :, :3]
		# image = np.array(image)
		# image = image.astype('float32') / 255
		image = image.convert("RGB")
		image = np.asarray(image, dtype=np.float32) / 255
		image = image[:, :, :3]
		return image
