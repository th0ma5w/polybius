import urllib
repo_file_encode = lambda x : urllib.quote_plus(x)

def repo_file_exists(repo,f):
	try:
		return open(repo+repo_file_encode(f))
	except:
		return None
