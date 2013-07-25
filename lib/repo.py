from git import *

def created_repo(repo):
	r = None
	try:
		r = Repo(repo)
	except:
		r = Repo.init(repo,bare=False)
		r = Repo(repo)
	return r
