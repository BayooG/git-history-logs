import git
import datetime

class RepoLog():
    local_branches = []
    remote_branches = []
    branches_log = {}
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.repo = git.Repo(path)
    
    @property
    def local_branches(self):
        return self.repo.heads
    
    @property
    def remote_branches(self):
        return [ref for ref in self.repo.refs if ref not in self.local_branches]
    
    
    def get_commits_log(self, branch, author):
        commits_lst = []
        last_month = datetime.datetime.now() + datetime.timedelta(-30)
        commits = list(self.repo.iter_commits(branch, max_count= 5000))
        for commit in commits:
            if commit.author.name == author and \
                 commit.committed_datetime.replace(tzinfo=None) > last_month.replace(tzinfo= None):
                     commits_lst.append(commit.message)
        return commits_lst

      