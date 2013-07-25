from lib.load_opml import loaded_opml
from lib.opml_links import links_list
from lib.cache_file import cached_file
from lib.load_feed import loaded_feed
from lib.load_feed_history import loaded_feed_history
from pprint import pprint
from lib.feedparser_jsonld import jsonld_from_feedparser
from lib.opml_jsonld import jsonld_from_opml
from lib.feedparser_html import html_from_feedparser
from urllib import unquote, quote
from uwsgi import cache_exists, cache_get, cache_set, cache_update

repo = './repo/'

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('static', filename='index.html'))

@app.route('/feed/<feedurl>')
def feed(feedurl):
	return jsonld_from_feedparser(loaded_feed(unquote(feedurl),repo).feed)

@app.route('/opml/<opmlurl>')
def opml(opmlurl):
	return jsonld_from_opml(loaded_opml(unquote(opmlurl),repo).opml)

@app.route('/memopml/<opmlurl>')
def memopml(opmlurl):
	if cache_exists(opmlurl):
		return cache_get(opmlurl)
	else:
		value = jsonld_from_opml(loaded_opml(unquote(opmlurl),repo).opml)
		cache_set(opmlurl,value,3600*24)
		return value

@app.route('/refresh/<feedurl>')
def refresh(feedurl):
	return jsonld_from_feedparser(loaded_feed(unquote(feedurl),repo,True).feed)

@app.route('/feed/html/<feedurl>')
def html_feed(feedurl):
	return html_from_feedparser(loaded_feed(unquote(feedurl),repo).feed)

@app.route('/entries/<feedurl>')
def feed_history(feedurl):
	return jsonld_from_feedparser(loaded_feed_history(unquote(feedurl),repo))

@app.route('/memfeed/<feedurl>')
def memfeed(feedurl):
	if cache_exists(feedurl):
		return cache_get(feedurl)
	else:
		value = jsonld_from_feedparser(loaded_feed(unquote(feedurl),repo).feed) 
		cache_set(feedurl,value,3600*24)
		return value

@app.route('/memrefresh/<feedurl>')
def memrefresh(feedurl):
	value = jsonld_from_feedparser(loaded_feed(unquote(feedurl),repo,True).feed)
	if cache_exists(feedurl):
		cache_update(feedurl,value,3600*24)
	else:
		cache_set(feedurl,value,3600*24)
	return value

