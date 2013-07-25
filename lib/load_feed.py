import feedparser
from cache_file import cached_file

class loaded_feed(cached_file):
	def __init__(self,feedurl,repo=None,force=False):
		feedparser.SANITIZE_HTML=0
		cached_file.__init__(self,feedurl,repo,force)
		feed = feedparser.parse(self.file_source)
		self.feed = feed
