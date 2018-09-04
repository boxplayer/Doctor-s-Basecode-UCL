import unittest
import python_app.apis.snomed_api as snomed_api

class TestSnomed(unittest.TestCase):

	def test_getDescription(self):
		result = snomed_api.getDescriptionById('679406011')
		self.assertEqual(result, "Methylphenyltetrahydropyridine (substance)")


if __name__ == '__main__':
	unittest.main()

