from load_feed import *

def clean_feedparser_object_for_json(o,l):
        for tag in l:
                if o.has_key(tag): o.pop(tag)
                [x.pop(tag) for x in o.entries if x.has_key(tag)]
                if o.feed.has_key(tag): o.feed.pop(tag)
	return o

def make_entries_from_summaries(o):
        for entry in o.entries:
                k=entry.keys()
                if 'content' not in k:
                        if 'summary' in k:
                                entry.update({'content': [{
                                        'base': u'',
                                        'type': u'text/html',
                                        'value': entry.summary,
                                        'language': None
                                }]})
        return o

