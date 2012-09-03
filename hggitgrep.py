import itertools
import os.path
import subprocess

def gitgrep(ui, repo, what, **opts):
    status = repo.status(clean=True)
    files = list(itertools.chain(status[0], status[1], status[4], status[6]))
    if files:
        subprocess.check_call(['git', 'grep', '--no-index', what] + files,
                              cwd=repo.root)

cmdtable = {"gitgrep": (gitgrep, [], "[what]")}
