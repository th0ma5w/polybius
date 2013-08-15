<img src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Polybios.jpg" alt="polybius statue" title="polybius" align="right" />

polybius
========

a feed reader backed by git

# how to start
1. git clone https://github.com/th0ma5w/polybius.git
2. pip install simplejson feedreader opml GitPython flask uwsgi
3. cd polybius/repo
4. git init
5. cd ..
6. ./start.sh
7. visit [http://127.0.0.1:3031/static/index.html#/opml/example.opml](http://127.0.0.1:3031/static/index.html#/opml/example.opml)
8. Edit update.sh with the double-quoted URL of the feed you like updated via script and schedule with cron

# features

- a hack, ready for customization 
- stores the original downloaded feed
- treats the commit log like a database
- retrieves historical items
- serves [json-ld](http://json-ld.org/)
- a mobile friendly example interface
- stands on the shoulders of giants

# example interface

- cobbled together with [bootstrap](http://getbootstrap.com/) and [angularjs](http://angularjs.org/)
- "works on my my machine" or in this case my phone

### opml subscriptions

<img src="https://pbs.twimg.com/media/BP_LsgACEAAcPf6.png" />

### feed display

<img src="https://pbs.twimg.com/media/BP_L6q8CAAAabVN.png" />


