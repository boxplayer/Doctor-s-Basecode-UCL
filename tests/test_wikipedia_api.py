import unittest
import package.apis.wikipedia_api as wikipedia_api

class TestWiki(unittest.TestCase):

	def test_getDescription(self):
		result = wikipedia_api.getDescription("Blood", 2)
		self.assertEqual(result, "Blood is a body fluid in humans and other animals that delivers necessary substances such as nutrients and oxygen to the cells and transports metabolic waste products away from those same cells.In vertebrates, it is composed of blood cells suspended in blood plasma. Plasma, which constitutes 55% of blood fluid, is mostly water (92% by volume), and contains proteins, glucose, mineral ions, hormones, carbon dioxide (plasma being the main medium for excretory product transportation), and blood cells themselves.")
		

if __name__ == '__main__':
	unittest.main()
