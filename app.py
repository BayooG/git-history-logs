# git-history-log

from pprint import pprint
from local import  TRILODOCS_PATH
from repolog import RepoLog

          
if __name__ == "__main__":
    repo = RepoLog(TRILODOCS_PATH)
    
    print('local branches')
    pprint(repo.local_branches)
    
    print('remote branches')
    pprint(repo.remote_branches)
    
    
    print('User commits on branch')
    branch_name = 'develop'
    author = 'Obay Daba'
    lst = repo.get_commits_log(branch_name, author)
    pprint(lst)
    