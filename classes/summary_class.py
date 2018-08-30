import os
import errno
import datetime
import json

class Summary:
	def __init__(self, medicine_list, symptom_list, anatomy_list, procedure_list, disease_list):
		self._medicine_list = medicine_list
		self._symptom_list = symptom_list
		self._anatomy_list = anatomy_list
		self._procedure_list = procedure_list
		self._disease_list = disease_list

	def quick_stats(self):

		med_len = len(self._medicine_list)
		sym_len = len(self._symptom_list)
		ana_len = len(self._anatomy_list)
		pro_len = len(self._procedure_list)
		dis_len = len(self._disease_list)
		total = med_len+sym_len+ana_len+pro_len+dis_len

		stats = {
			"medicine_mentions":med_len,
			"symptom_mentions":sym_len,
			"anatomy_mentions":ana_len,
			"procedure_mentions":pro_len,
			"disease_mentions":dis_len,
			"total_entities_found":total
		}
		return stats

	def get_medicine_list(self):
		return self._medicine_list

	def get_symptom_list(self):
		return self._symptom_list

	def get_anatomy_list(self):
		return self._anatomy_list

	def get_procedure_list(self):
		return self._procedure_list

	def get_disease_list(self):
		return self._disease_list


	def toJSON(self):
		#create directory
		now = datetime.datetime.now()
		now = now.replace(microsecond=0)

		try:
			os.makedirs(os.path.dirname("package/data/{}/".format(now)))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

		main = [self._medicine_list, self._symptom_list, self._anatomy_list, self._procedure_list, self._disease_list]

		jsonFILE = json.dumps(main, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)
		print("Writing JSON")
		json_file = open('package/data/{}/summary.json'.format(now), 'w+')
		json_file.write(jsonFILE)
		json_file.close()
		print("JSON saved!")

	def to_txt(self):
		try:
			os.makedirs(os.path.dirname("package/data/{}/pubmed_articles/".format(now)))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

		pubmed_articles = open("package/data/{}/pubmed_articles/".format(now), "w+")

		pubmed_articles.write()











