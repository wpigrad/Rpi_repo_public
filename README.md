# Rpi_repo_public
raspberry pi repository open to public

Git is an open source distributed version (source) control system by Linus Torvalds.
Alternative: Gitlab, Bitbucket

working directory / staging area / local repo / remote repo / stash


$ ls -la .git

##############################################################################
# initial setup
##############################################################################

# install
$ sudo apt install git-all

# create new repo on github
$ curl -w "user_name" https;//api.github.com/user/repos -d '{"name":"Repo_name","private":false}'

# clone from remote github repo to local repo
$ git clone https://github.com/wpigrad/Repo_name.git

# pull the latest version of the remote git repo while in the local repo
$ cd Repo_name
$ git pull

# add compares local files with remote repo master
$ git add --all or $ git add .
$ git status

# config credentials only done once when first setting up local repo
$ git config --global user.email"user_email@gmail.com"
$ git config --global user.name "user_name"
$ git congig --global credential.helper store

# commit
$ git commit -m "Added content to READ.md and added python.py files"
$ git status
$ git log

# push to remote repo
$ git push -u origin master

##############################################################################
# normal git commit and push
##############################################################################

# pull
$ git fetch
$ git merge
$ git pull

# add
$ git add --all or $ git add .
$ git status
$ echo [private_file] > .gitignore

# commit
$ git commit -m "Add a comment here about the revision."
$ git status
$ git log
$ git log --oneline
$ git log --patch -1 (q to quit)

# push
$ git push -u origin master

##############################################################################
# create a new repo on the command line from the working directory
##############################################################################

$ git init
$ git add .
$ git status
$ git commit -m "Initial Commit"
$ git log
$ git remote add origin git@github.com:wpigrad/Repo_name.git
$ git push -u origin maaster

##############################################################################
# push an existing repo from the command line
##############################################################################

$ git remote add origin git@githum.com:wpigrad/Repo_name.git
$ git branch -M main
$ git push -u origin main

##############################################################################
# branch
##############################################################################

$ git branch feature
$ git branch
$ git switch feature
$ git checkout feature
$ git branch
$ git commit -am "Added Feature"
$ git push --set-upstream origin feature

##############################################################################
# revert to previous code base
##############################################################################

$ git diff [commit-hash1] [commit-hash2]
$ git log
$ git revert [commit-hash]
$ git cherry-pick [commit-hash?]

$ git reset --hard [commit-hash]
$ git push --force origin master
