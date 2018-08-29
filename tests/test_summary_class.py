import unittest
from package.classes.summary_class import Summary

class TestSummary(unittest.TestCase):

	def test_summary(self):
		sum_1 = Summary(["Aspirin"], ["Pain"], ["Bone"], ["Operation"], ["Leprocy"])

		stats = {
			"medicine_mentions":1,
			"symptom_mentions":1,
			"anatomy_mentions":1,
			"procedure_mentions":1,
			"disease_mentions":1,
			"total_entities_found":5
		}
		
		self.assertEqual(sum_1.quick_stats(), stats)

		# wiki = ent_1.wikipedia_description()
		# self.assertIsNone(wiki)

		# ent_1.get_wikipedia_description(2)
		# self.assertEqual(ent_1.wikipedia_description(), "Aspirin, also known as acetylsalicylic acid (ASA), is a medication used to treat pain, fever, or inflammation. Specific inflammatory conditions in which aspirin is used include Kawasaki disease, pericarditis, and rheumatic fever.")


if __name__ == '__main__':
	unittest.main()
