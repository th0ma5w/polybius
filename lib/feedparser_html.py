from clean_feedparser import clean_feedparser_object_for_json, make_entries_from_summaries
import time

def html_from_feedparser(parsed):
	parsed = make_entries_from_summaries(parsed)
	feed = parsed['feed']
	entries = parsed['entries']
	output  = "<h1>%s</h1>\n" % feed.title
	output += "<h3>%s</h3>\n" % feed.subtitle
	if feed.has_key('updated_parsed') and feed['updated_parsed'] is not None:
		output += "<h4>%s</h4>\n" % time.strftime('%D %T %Z',feed.updated_parsed)
	for entry in entries:
		output += '<h2><a href="%s">%s</a></h2>\n' % (entry.link,entry.title)
		if entry.has_key('updated_parsed') and entry['updated_parsed'] is not None:
			output += "<h4>%s</h4>" % time.strftime('%D %T %Z',entry.updated_parsed)
		output += "%s" % entry.content[0]['value']
	return output
