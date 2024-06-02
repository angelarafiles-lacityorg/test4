import os

branches=list(os.popen("git branch -a|grep -v '>'|grep remotes|sed 's,^.*origin/,,g'").read().splitlines())
branch=branches[0]
for branch in branches:
    cmdstr=f"git switch {branch}"
    print(os.popen(cmdstr).read())
    cmdstr=f"git log --oneline --reverse refs/heads/{branch} | awk 'NR % 500 == 0'|cut -d ' ' -f 1"
    commits=list(os.popen(cmdstr).read().splitlines())
    for commit in commits:
        cmdstr=f"git push origin {commit}:refs/heads/{branch}"
        print(os.popen(cmdstr).read())

