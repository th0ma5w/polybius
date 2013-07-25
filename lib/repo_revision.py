import git

def file_revision(repo,revision,filename):
	r = git.Repo(repo)
	return r.rev_parse(revision + ':' + filename).data_stream.read()
