from url_encoding import repo_file_exists, repo_file_encode
import urllib2

class cached_or_not:
	def __init__(self,fileurl,repo=None,force=False):
		self.fileurl=fileurl
		self.repo=repo
		self.encoded_url = repo_file_encode(fileurl)
		repo_file = repo_file_exists(repo,fileurl)
		self.cached = True
		if repo_file is not None and not force:
			file_source = repo_file.read()
		if repo_file is None or force:
			try:
				f = urllib2.urlopen(fileurl)
				file_source = f.read()
				f.close()
				self.cached = False
			except:
				if repo_file is not None:
					file_source = repo_file.read()
		self.file_source = file_source
