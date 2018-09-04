import requests
import json
import os
import errno
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError



# NCBI api key allowing 10 queries per second PER API KEY! (default 3 per second)
api_key = "4ab7fdeb020e490db266f2bcca7c5056f709"


def esearch(term, max_articles, max_article_age, output_format="json"):

	## returns article UIDs for given search term ##

	print("Searching for articles on {}.......".format(term))

	# spaces must be replaced by +'s
	search_term = term.replace(" ", "+")

	# choose a database
	db = "pubmed"

	# max amount of articles
	retmax = max_articles

	# maximum age of articles (days)
	reldate = max_article_age

	# output format
	retmode = output_format  


	url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={}&term={}&reldate={}&datetype=edat&retmode={}&retmax=10&usehistory=y&api_key={}".format(db, search_term, reldate, retmode, api_key)

	# try to get a response
	try:
		response = urlopen(url).read()
	except HTTPError as e:
		content = e.read()
		print(e)
		return None

	# extract data from response
	data = json.loads(response.decode('utf-8'))


	# save to json file
	request = requests.get(url)
	req_list = request.json()

	# open new file in directory and save the data as json
	filename = "python_app/data/entrez/esearch_{}.json".format(term)
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
		except OSError as exc:
			print("Couldn't create directory")

	json_file = open(filename, 'w+')
	json_file.write(json.dumps(req_list))
	json_file.close()
	print("Json esearch created")

	print("Article Download Complete.")

	return data['esearchresult']['idlist']


def esummary(uids):

	## retrieves a summary of articles by UIDs ##

	# database to retrieve articles from
	db = "pubmed"

	# list of article UIDs
	uid_list = ",".join(uids)

	# uid_list = "11850928,11482001"

	# output format
	retmode = "json"

	url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db={}&id={}&datetype=edat&retmode={}&api_key={}".format(db, uid_list, retmode, api_key)

	request = urlopen(url).read()
	data = json.loads(request.decode('utf-8'))

	# to json file
	request = requests.get(url)
	req_list = request.json()

	# open new file in directory and save the data as json

	print("Downlading esummary to json")
	filename = "python_app/data/entrez/esummary.json"
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
		except OSError as exc:
			print("Couldn't create directory")

	json_file = open(filename, 'w+')
	json_file.write(json.dumps(req_list))
	json_file.close()
	print("Json esummary created")

	summary_list = []
	for uid in uids:
		summary_list.append(data['result'][uid])

	# for thing in summary_list:
	# 	print("THING: ", thing)

	print("Articles Summary Download Complete.")
	return summary_list

# def efetch():

	

