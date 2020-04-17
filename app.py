# git-history-log

from pprint import pprint
from local import  TRILODOCS_PATH

import git


r = git.Git(TRILODOCS_PATH)
repo = git.Repo(TRILODOCS_PATH)
origins_lst = [i for i in  repo.refs if i.name.startswith('origin')]



pprint(repo.branches)