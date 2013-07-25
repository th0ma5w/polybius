from cache_or_not import cached_or_not
from repo import created_repo

class cached_file(cached_or_not):
	def __init__(self,fileurl,repo,force=True):
		self.repo=repo
		self.gitrepo = created_repo(repo)
		self.fileurl=fileurl
		cached_or_not.__init__(self,fileurl,repo,force)
		if not self.cached: 
			self.commit()
	def commit(self):
		with open(self.repo+self.encoded_url,'w') as f:
			f.write(self.file_source)
		self.gitrepo.index.add([self.encoded_url])
		if self.gitrepo.is_dirty():
			return self.gitrepo.index.commit(self.fileurl)
