from urllib.request import urlopen
from urllib.parse import quote
import json

def getDescriptionById(id):

	baseUrl = 'http://browser.ihtsdotools.org/api/v1/snomed/'
	edition = 'en-edition'
	version = 'v20180131'

	url = baseUrl + edition + '/' + version + '/descriptions/' + id
	response = urlopen(url).read()
	data = json.loads(response.decode('utf-8'))

	try:
		return_data = data['matches'][0]['term']
	except IndexError:
		print("Index Error snomed API")
		return None

	return return_data

def getConceptById(id):

	baseUrl = 'http://browser.ihtsdotools.org/api/v1/snomed/'
	edition = 'en-edition'
	version = 'v20180131'
	
	url = baseUrl + edition + '/' + version + '/concepts/' + id
	response = urlopen(url).read()
	data = json.loads(response.decode('utf-8'))

	return data['fsn']


def getDescriptionsByString(searchTerm):

	baseUrl = 'http://browser.ihtsdotools.org/api/v1/snomed/'
	edition = 'en-edition'
	version = 'v20180131'

	url = baseUrl + edition + '/' + version + '/descriptions?query=' + quote(searchTerm) + '&limit=50&searchMode=partialMatching&lang=english&statusFilter=activeOnly&skipTo=0&returnLimit=100&normalize=true'
	response = urlopen(url).read()
	data = json.loads(response.decode('utf-8'))

	# return data['details']['total']
	return data['details']['total']

def getDescriptionsByStringFromProcedure(searchTerm, semanticTag):

	baseUrl = 'http://browser.ihtsdotools.org/api/v1/snomed/'
	edition = 'en-edition'
	version = 'v20180131'

	url = baseUrl + edition + '/' + version + '/descriptions?query=' + quote(searchTerm) + '&limit=50&searchMode=partialMatching&lang=english&statusFilter=activeOnly&skipTo=0&returnLimit=100&semanticFilter=' + quote(semanticTag) + '&normalize=true'
	response = urlopen(url).read()
	data = json.loads(response.decode('utf-8'))

	return data['details']['total']

# if __name__ == "__main__":
# 	main()
