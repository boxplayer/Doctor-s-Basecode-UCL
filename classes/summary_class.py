import os
import errno
# import datetime
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


	def toJSON(self, now):
		#create directory
		# now = datetime.datetime.now()
		# now = now.replace(microsecond=0)

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

	def to_txt(self, now):

		try:
			os.makedirs(os.path.dirname("package/data/{}/articles/".format(now)))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

		medicine_articles = open("package/data/{}/articles/medicine_articles.txt".format(now), "w+")
		symptom_articles = open("package/data/{}/articles/symptom_articles.txt".format(now), "w+")
		anatomy_articles = open("package/data/{}/articles/anatomy_articles.txt".format(now), "w+")
		procedure_articles = open("package/data/{}/articles/procedure_articles.txt".format(now), "w+")
		disease_articles = open("package/data/{}/articles/disease_articles.txt".format(now), "w+")

		# all_list = [self._medicine_list, self._symptom_list, self._anatomy_list, self._procedure_list, self._disease_list]

		# for _list in lists:
		# 	for medicine in _list:
		# 		articles = medicine.medical_articles()
		# 		name = medicine.name()
		# 		medicine_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
		# 		for article in articles:
		# 			medicine_articles.write("--UID: {} \n".format(article['uid']))
		# 			medicine_articles.write("--Date: {} \n".format(article['pubdate']))
		# 			medicine_articles.write("--Last Author: {} \n".format(article['lastauthor']))
		# 			medicine_articles.write("--Title: {} \n".format(article['title']))

		# 		medicine_articles.write(" \n \n \n ")

		# 	medicine_articles.close()


		for medicine in self._medicine_list:
			articles = medicine.medical_articles()
			name = medicine.name()
			medicine_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
			for article in articles:
				medicine_articles.write("--UID: {} \n".format(article['uid']))
				medicine_articles.write("--Date: {} \n".format(article['pubdate']))
				medicine_articles.write("--Last Author: {} \n".format(article['lastauthor']))
				medicine_articles.write("--Title: {} \n".format(article['title']))

			medicine_articles.write(" \n \n \n ")

		medicine_articles.close()



		for symptom in self._symptom_list:
			articles = symptom.medical_articles()
			name = symptom.name()
			symptom_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
			for article in articles:
				symptom_articles.write("--UID: {} \n".format(article['uid']))
				symptom_articles.write("--Date: {} \n".format(article['pubdate']))
				symptom_articles.write("--Last Author: {} \n".format(article['lastauthor']))
				symptom_articles.write("--Title: {} \n".format(article['title']))

			symptom_articles.write(" \n \n \n ")

		symptom_articles.close()


		for anatomy in self._anatomy_list:
			articles = anatomy.medical_articles()
			name = anatomy.name()
			anatomy_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
			for article in articles:
				anatomy_articles.write("--UID: {} \n".format(article['uid']))
				anatomy_articles.write("--Date: {} \n".format(article['pubdate']))
				anatomy_articles.write("--Last Author: {} \n".format(article['lastauthor']))
				anatomy_articles.write("--Title: {} \n".format(article['title']))

			anatomy_articles.write(" \n \n \n ")

		anatomy_articles.close()


		for procedure in self._procedure_list:
			articles = procedure.medical_articles()
			name = procedure.name()
			procedure_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
			for article in articles:
				procedure_articles.write("--UID: {} \n".format(article['uid']))
				procedure_articles.write("--Date: {} \n".format(article['pubdate']))
				procedure_articles.write("--Last Author: {} \n".format(article['lastauthor']))
				procedure_articles.write("--Title: {} \n".format(article['title']))

			procedure_articles.write(" \n \n \n ")

		procedure_articles.close()


		for disease in self._disease_list:
			articles = disease.medical_articles()
			name = disease.name()
			disease_articles.write("---PUBMED ARTICLES: {} \n \n ".format(name))
			for article in articles:
				disease_articles.write("--UID: {} \n".format(article['uid']))
				disease_articles.write("--Date: {} \n".format(article['pubdate']))
				disease_articles.write("--Last Author: {} \n".format(article['lastauthor']))
				disease_articles.write("--Title: {} \n".format(article['title']))

			disease_articles.write(" \n \n \n ")

		disease_articles.close()






