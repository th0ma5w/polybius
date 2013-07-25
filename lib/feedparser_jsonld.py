import simplejson
from qname import qname
from clean_feedparser import clean_feedparser_object_for_json, make_entries_from_summaries

ctx = qname("http://www.w3.org/2005/Atom#","feed,entry,title,link,updated,author,id,summary,content")

def jsonld_from_feedparser(parsed):
	ld_doc={}
	parsed = make_entries_from_summaries(clean_feedparser_object_for_json(parsed, ['updated_parsed','published_parsed']))
	feed = parsed['feed']
	entries = parsed['entries']
	ld_doc.update({"@context":ctx,"feed":feed,"entry":entries})
	return simplejson.dumps(ld_doc)

