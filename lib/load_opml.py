import opml
from cache_file import cached_file

class loaded_opml(cached_file):
	def __init__(self,opmlurl,repo=None,force=False):
		cached_file.__init__(self,opmlurl,repo,force)
		o = opml.from_string(self.file_source)
		self.opml = o
