import feedparser
from repo_log import file_commit_history
from repo_revision import file_revision
from url_encoding import repo_file_encode

def loaded_feed_history(feedurl,repo,count=5,start=0,step=1):
	feedparser.SANITIZE_HTML=0
	feed_filename = repo_file_encode(feedurl)
	revisions = file_commit_history(repo,feed_filename)[start:start+count:step]
	historical_feed = None
	for feed_revision in revisions:
		feed_revision_source = file_revision(repo,feed_revision,feed_filename)
		if not historical_feed:
			historical_feed = feedparser.parse(feed_revision_source)
		else:
			previous_revision = feedparser.parse(feed_revision_source)
			historical_feed.entries += [x for x in previous_revision.entries 
							if x not in historical_feed.entries]
	return historical_feed
