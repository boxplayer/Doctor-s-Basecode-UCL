import package.apis.wikipedia_api as wikipedia_api
import package.apis.snomed_api as snomed_api
import package.apis.entrez_api as entrez_api
import json
import os


class Entity:

	#TODO create 5 different constructors

	def __init__(self, name, subject, snomed_code, typ):
		# required entity parameters
		self._name = name
		self._snomed_code = snomed_code
		self._type = typ

		# contextual information
		self._subject = subject

		# downloadable extras
		self._wiki = None
		self._img = None
		self._snomed_term = None

		# downloadable articles
		self._articles = None


	def __init__(self, name, subject, snomed_code, typ, medication_route, medication_allergy, medication_strength, medication_frequency, medication_duration, medication_dosage, symptom_body_laterality, symptom_history, symptom_duration, symptom_start_time, symptom_severity, symptom_body_location, anatomy_body_laterality, anatomy_body_side, procedure_duration, procedure_method, procedure_start_time, procedure_end_time, procedure_body_location, procedure_device, disease_course, disease_start_time, disease_end_time, disease_associated_symptom, disease_body_location, disease_severity, disease_alleviating_factor, disease_exacerbating_factor):

		# required entity parameters
		self._name = name
		self._snomed_code = snomed_code
		self._type = typ

		# contextual information
		self._subject = subject

		# medical contextual information
		self._medication_route = medication_route
		self._medictaion_allergy = medication_allergy
		self._medication_strength = medication_strength
		self._medication_frequency = medication_frequency
		self._medication_duration = medication_duration
		self._medication_dosage = medication_dosage

		# symptom contextual information
		self._symptom_body_laterality = symptom_body_laterality
		self._symptom_history = symptom_history
		self._symptom_duration = symptom_duration
		self._symptom_start_time = symptom_start_time
		self._symptom_severity = symptom_severity
		self._symptom_body_location = symptom_body_location

		# anatomy contextual information
		self._anatomy_body_laterality = anatomy_body_laterality
		self._anatomy_body_side = anatomy_body_side

		# procedure contextual information
		self._procedure_duration = procedure_duration
		self._procedure_method = procedure_method
		self._procedure_start_time = procedure_start_time
		self._procedure_end_time = procedure_end_time
		self._procedure_body_location = procedure_body_location
		self._procedure_device = procedure_device

		# disease contextual information
		self._disease_course = disease_course
		self._disease_start_time = disease_start_time
		self._disease_end_time = disease_end_time
		self._disease_associated_symptom = disease_associated_symptom
		self._disease_body_location = disease_body_location
		self._disease_severity = disease_severity
		self._disease_alleviating_factor = disease_alleviating_factor
		self._disease_exacerbating_factor = disease_exacerbating_factor

		# downloadable extras
		self._wiki = None
		self._img = None
		self._snomed_term = None

		# downloadable articles
		self._articles = None



	### DOWNLOADERS

	# if available download wikipedia description of entity
	def get_wikipedia_description(self, sentences):
		self._wiki = wikipedia_api.getDescription(self._name, sentences)

	# if available get image of entity from wikipedia
	def get_image(self):
		self._img = wikipedia_api.getImage(self._name)

	# get snomed term using snomed code
	def get_snomed_term(self):
		self._snomed_term = snomed_api.getConceptById(self._snomed_code)

	# get pubmed articles about the term
	def get_articles(self, max_articles="10", max_article_age="60"):
		uid_list = entrez_api.esearch(self._name, max_articles, max_article_age)
		if(uid_list == None):
			print("Downloading articles failed.")
			return
		articles = entrez_api.esummary(uid_list)
		self._articles = articles





	### PRINTERS

	def printAll(self):
		print(self._type.upper())

		print("--",self._name)

		if(self._snomed_term!=None):
			print('--',self._snomed_term)

		print("--",self._snomed_code)

		if(self._subject != None):
			print("--",self._subject)

		if(self._wiki!= None):
			print(self._wiki)

		if(self._img!=None):
			print(self._img)


	def printArticles(self):
		if(self._articles == None):
			print("No articles to print. Please download articles first.")
			return

		print("----ARTICLES LIST----")
		print("TERM: {}".format(self._name))
		for article in self._articles:
			print("--UID: {}".format(article['uid']))
			print("--Date: {}".format(article['pubdate']))
			print("--Last Author: {}".format(article['lastauthor']))
			print("--Title: {}".format(article['title']))
			print(" ")
		print("------END LIST------")



	### GETTERS

	def type(self):
		return self._type

	def name(self):
		return self._name

	def subject(self):
		return self._subject

	def snomed_code(self):
		return self._snomed_code

	def snomed_term(self):
		return self._snomed_term

	def wikipedia_description(self):
		return self._wiki

	def medical_articles(self):
		return self._articles

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)

