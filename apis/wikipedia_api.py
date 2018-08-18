import wikipedia

def getDescription(term, no_sentences):
	print("Downloading wikipedia description...")
	try:
		summary = wikipedia.summary(term, sentences = no_sentences)
	except wikipedia.exceptions.DisambiguationError:
		# too much ambiguity
		print("DisambiguationError: Couldn't download wikipedia description.")
		return
	except wikipedia.exceptions.PageError:
		print("PageError: Couldn't download wikipedia description.")
		return
	except:
		print("Error: Couldn't download wikipedia description.")
		return

	print("Successful description download!")
	return summary

def getImage(term):
	print("Downloading image...")

	try:
		page = wikipedia.page(term)
	except wikipedia.exceptions.DisambiguationError:
		print("DisambiguationError: Couldn't download image.")
		return
	except wikipedia.exceptions.PageError:
		print("PageError: Couldn't download image.")
		return
	except:
		print("Error: Couldn't download image.")
		return

	try:
		img = page.images[0]
	except IndexError:
		print("Error: Image doesn't exist!")
		return

	print("Successful image download!")
	return img