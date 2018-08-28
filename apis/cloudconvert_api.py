import cloudconvert

def main(input_file):

	api = cloudconvert.Api('X0LnpbqjPzPCKTWJAh50nMORz0olrqfJHHJ9gYFaQRfBuwv7QaEmmUPpwftXiAuY')

	process = api.convert({
	    'inputformat': 'pdf',
	    'outputformat': 'txt',
	    'input': 'upload',
	    'file': open('{}'.format(input_file), 'rb')
	})
	process.wait() # wait until conversion finished
	process.download("package/output.txt") # download output file