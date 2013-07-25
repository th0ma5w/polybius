import git

garbage_collect = lambda repo: git.Git(repo).gc()
