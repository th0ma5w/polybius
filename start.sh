uwsgi --http :3031 --wsgi-file webtest1.py --callable app --static-map /static=./static --threads 4 --processes 4 --cache2 name=default,items=500,blocksize=2000000
