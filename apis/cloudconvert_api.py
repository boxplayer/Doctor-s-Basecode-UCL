import cloudconvert

def main(input_file):

	inputformat = "pdf"
	outputformat = "txt"

	api = cloudconvert.Api('X0LnpbqjPzPCKTWJAh50nMORz0olrqfJHHJ9gYFaQRfBuwv7QaEmmUPpwftXiAuY')

	process = api.convert({
	    'inputformat': inputformat,
	    'outputformat': outputformat,
	    'input': 'upload',
	    'file': open('{}'.format(input_file), 'rb')
	})
	process.wait() # wait until conversion finished
	print("downloading converted file....")
	process.download("package/output.{}".format(outputformat)) # download output file