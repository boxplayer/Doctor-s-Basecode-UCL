import unittest
from package.classes.entity_class import Entity

class TestEntity(unittest.TestCase):

	def test_entity(self):
		ent_1 = Entity("Aspirin", "Patient", "391788009", "medicine")
		self.assertEqual(ent_1.snomed_code(), "391788009")

		wiki = ent_1.wikipedia_description()
		self.assertIsNone(wiki)

		ent_1.get_wikipedia_description(2)
		self.assertEqual(ent_1.wikipedia_description(), "Aspirin, also known as acetylsalicylic acid (ASA), is a medication used to treat pain, fever, or inflammation. Specific inflammatory conditions in which aspirin is used include Kawasaki disease, pericarditis, and rheumatic fever.")


if __name__ == '__main__':
	unittest.main()
