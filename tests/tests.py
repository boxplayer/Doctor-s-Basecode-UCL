from python_app.tests.test_entity_class import TestEntity
from python_app.tests.test_summary_class import TestSummary
from python_app.tests.test_wikipedia_api import TestWiki
from python_app.tests.test_snomed_api import TestSnomed
import unittest


if __name__ == '__main__':
	
	tests_to_run = [TestEntity, TestSummary, TestWiki, TestSnomed]

	loader = unittest.TestLoader()

	suites_list = []
	for test_class in tests_to_run:
		test = loader.loadTestsFromTestCase(test_class)
		tests_list.append(test)

	big_tests = unittest.TestSuite(tests_list)

	runner = unittest.TextTestRunner()
	results = runner.run(big_tests)
