import itertools
import os.path
import subprocess
import sys

def gitgrep(ui, repo, what, **opts):
    status = repo.status(clean=True)
    files = list(itertools.chain(status[0], status[1], status[4], status[6]))
    if not files:
        sys.exit('no files in repo')
    cmd = ['git', 'grep', '--no-index', what] + files
    sys.exit(subprocess.call(cmd, cwd=repo.root))

cmdtable = {"gitgrep": (gitgrep, [], "[what]")}
