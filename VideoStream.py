'''
class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0

	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data:
			framelength = int(data)

			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data

	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
'''

from PIL import Image
from libmaix import Camera
import io

class V831VideoCapture(VideoCapture):

		def __init__(self, source="/sipeed/v831", size=(640, 480)):
			self.source = source
			self.width, self.height = size
			self.cam = Camera(self.width, self.height)

		def read(self):
			return self.cam.read()  # bytes

		def capture(self):
			return Image.frombytes("RGB", (self.width, self.height), self.read())

		def __del__(self):
			self.cam.close()


class VideoStream:
  
 	def __init__(self, filename):
		self.filename = filename
		self.camera = V831VideoCapture()
		self.frameNum = 0

	def nextFrame(self):
		tmp = io.BytesIO()
		self.camera.capture().save(tmp, format='jpeg', quality=95)
		self.frameNum += 1
		return tmp.read()

	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
