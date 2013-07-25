import git

def file_commit_history(repo,filename):
	g = git.Repo(repo)
	hexshas = [x.hexsha for x in g.iter_commits(paths=filename)]
	return hexshas
