import json
import sys
import os
import subprocess
import re
import argparse
import shutil
import pathlib

verbose=False
import logs

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# This script marks code and comments you should read first
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# python features:
# Command Line Argument Parsing
# with open(file, 'r' as f
# json.load()
# [] - lists

# os.path.exists(dir)
# os.walk(repo_search_path
# os.makedirs(dir, exist_ok=True)
# os.symlink(target, symlink)
# os.chdir(dir)
# os.path.exists(dir)
# os.path.isfile(args.suite_json_file)
# os.path.isdir
# os.environ['DEV1_SUITES']
# os.path.islink(symlink)
# os.path.join

# result = subprocess.run([args], capture_output=True, check=False) 
# subprocess.CompletedProcess object
# subprocess.CompletedProcess.stdout
# subprocess.CompletedProcess.returncode

# ''' multi-line literal '''

# shutil.rmtree(dir) 
# shutil.copytree

# pathlib.Path().touch

# def f()
# return
# exit()

# Git Features:

# git clone url name
# git add .
# git commit -m
# git push -u origin branch
# git init --bare -b branch
# git remote add upstream
# git reverse-parse -- verify branch
# git worktree add wortree_path branch

# Actions this script will take with regard to 
# Repositories
#
#   Creates a bare repository in <suite-dir>/repositories/<repo-name>.git
#   via git-init, copytree or git clone
#
# Tasks
#   Creates a directory in <suite-dir>/tasks/
#   for each task
#   Creates a worktree for each unique branch/repository combination
#   found for all tasks
#   Creates a symlink for each worktree required for a task
#   Creates additional symlinks in specific directories as specified.
#   
# - - - - - - - - - - - - - - - - - 
suites_dir=os.environ['DEV1_SUITES']
# - - - - - - - - - - - - - - - - - 

repository_search_paths=[]

argParser = argparse.ArgumentParser()
argParser.add_argument('suite_json_file', 
                       type=str,
                       help="The json file describing an application suite's structure")
argParser.add_argument('repository_search_paths', 
                       type=str,
                       nargs='*',
                       help="search paths for previously cloned repositories")
argParser.add_argument('-v', '--verbose',
                       action='store_true',
                       
                       help='Verobose Logging')

args=argParser.parse_args()
logs.verbose=args.verbose
logs.verbose=True
l=len("Suite Specification Json:")
logs.log_labeled("Suite Specification Json", args.suite_json_file, l,0)
logs.log_labeled("Repository Search_Paths ", args.repository_search_paths, l,0)
# - - - - - - - - - - - - -
def make_folders( dir):
  if not os.path.exists(dir):
    os.makedirs(dir, exist_ok=True)
    logs.log_labeled("Create Folder:", dir)
  else:
    logs.log_labeled("Previously Created Folder:", dir)
    
#-----------------
def create_symlink(target,symlink):
  if not os.path.islink(symlink):
    os.symlink(target, symlink)
    logs.log_labeled( "Created_symlink", symlink + "->" + target)
  else:
    logs.log_labeled( "Found existing symlink", symlink + "->" + target)
 
def chdir(dir):
   os.chdir(dir)      
   logs.log_labeled("Change Folder", dir)
def rm_tree(dir):
   shutil.rmtree(dir)      
   logs.log_labeled("Remove Folder", dir)
   
#------------
def copy_repo( repositories_dir,repo_copy_path, repo_path ):
  if not os.path.exists(repo_copy_path):
    logs.log_labeled("Git repo to copy not found", repo_copy_path)
    return 1

  if not os.path.exists(repo_path):
    logs.log("Executing shutil.copytree(" + repo_copy_path + ", " + repo_path+")")
    shutil.copytree( repo_copy_path, repo_path)
    logs.log_labeled("Change Folder:  ", repo_path)
    chdir(repo_path)
    run_result = subprocess.run(["git", "rev-parse", "--is-bare-repository"], text=True, capture_output=True, check=False)
    if run_result.stdout == "false\n":
      run_result = subprocess.run(["git", "config", "--bool", "core.bare", "true"],text=True, capture_output=True, check=False)
  else:
    logs.log_labeled("Previously Created Git Repo", repo_path)
    
#------------
def git_init(repositories_dir, repo_name, branch):
  repo_path=os.path.join(repositories_dir,repo_name+".git")
  
  if not os.path.exists(repo_path):

    chdir(repositories_dir)
    run_result = subprocess.run(["git", "init", "--bare", "-b", branch, repo_path], capture_output=True, check=False)
    logs.log("git init --bare "+ repo_path,space_after=1)
    DEV1_CONTEXT_CACHE_PATH=os.environ['DEV1_CONTEXT_CACHE_PATH']
    chdir(DEV1_CONTEXT_CACHE_PATH)
    dev1_user_temp=os.path.join(DEV1_CONTEXT_CACHE_PATH, 'temp')
    run_result = subprocess.run(["git", "clone", repo_path, 'temp'], capture_output=True, check=False)
    chdir(dev1_user_temp)
    pathlib.Path(os.path.join(dev1_user_temp,'build.sh')).touch()
    pathlib.Path(os.path.join(dev1_user_temp,'run.sh')).touch()
    run_result = subprocess.run(["git", "add", "."], capture_output=True, check=False)
    run_result = subprocess.run(["git","commit", "-m", "empty build.sh and run.sh files"], capture_output=True, check=False)
    run_result = subprocess.run(["git", "remote", "add", "origin", repo_path], capture_output=True, check=False)
    run_result = subprocess.run(["git", "push", "-u", "origin", branch], capture_output=True, check=False)
    rm_tree(dev1_user_temp)

  else:
    logs.log_labeled("Previously created git repo:", repo_path )
    
  worktree_path=os.path.join(worktrees_dir, branch, repo_name )
  create_worktree(repositories_dir, repo_name, branch, worktree_path)
   
#-------------
def clone_repo( repositories_dir, repository_path, repository_name, branch, origin, upstream):
  if not os.path.exists(repository_path):
    logs.log_labeled("clone repo", [repository_name, branch, origin, upstream])
    logs.log_labeled("Change Folder:  ", repositories_dir)
    os.chdir(repositories_dir)
    repository_git=repository_name+".git"
    url=None
    if origin != None:
      url = origin
    if url == None:
      url = upstream
    if url != None:
      logs.log("git clone --bare "+ url + " " + repository_git)  
      run_result = subprocess.run(["git", "clone", "--bare", url, repository_git], capture_output=True, check=False)
      chdir (repository_git)
    if upstream != "":
      chdir(os.path.join(repositories_dir,repository_git))
      run_result = subprocess.run([ "git", "remote", "add", "upstream", repo_upstream], capture_output=True, check=False)
  else:
    logs.log_labeled("Git repo found", repo_path)
 
#----------------
def create_branch(repositories_dir, repository_name, _branch):
  run_result = subprocess.run(["git", "rev-parse", "--verify", _branch], text=True, capture_output=True, check=False)
  if run_result.returncode != 0:
    run_result = subprocess.run(["git", "branch", _branch], text=True, capture_output=True, check =False)
  logs.log_labeled("create_branch", [repositories_dir, repository_name, _branch])
  return 0
      
#------------------
def create_worktree(repositories_dir, repository_name, _branch, worktree_path):
  chdir(os.path.join(repositories_dir, repository_name+".git"))
  if not os.path.exists(os.path.dirname(worktree_path)):
    subprocess.run (["mkdir", "-p",  os.path.dirname(worktree_path) ])
  if not os.path.exists(worktree_path):
    run_result = subprocess.run(["git", "worktree", "add", worktree_path, _branch])
    logs.log_labeled("create_worktree", [repository_name, _branch, worktree_path])
  else:
    logs.log_labeled("Previously Created Worktree", [repository_name, _branch, worktree_path])
   
# - - - - - - - - - - - - - - - - - - - 
# defined: args.suite_json_file
#          args.repository_search_paths
#          verbose
#          help
# - - - - - - - - - - - - - - - - - - - 
#--------------------------
def find_repository_to_copy (repository_name, repo_search_path):
  if repo_search_path != None:
    if not os.path.exists(repo_search_path):
      logs.log_labeled ("Error - Could not find repository search path", repo_search_path)
      exit()
    repositories_for_copy=[]
    for root, dirs, files in os.walk(repo_search_path):
      for dir in dirs:
        if dir == ".git":
          repositories_for_copy.append(os.path.join(root,dir))
    for path in repositories_for_copy:
      if re.search(r"/"+repository_name+"/.git", path):
        return path
  return ""
 
#-------------
# global scope  
#-------------
if not os.path.isfile(args.suite_json_file):  
  print ("Error: bootstrap.py ", args.suite_json_file, " not found.")


with open(args.suite_json_file, 'r') as f:
  
  # - - - - - - - - - - - - 
  suite_spec = json.load(f)
  # - - - - - - - - - - - - 
label_len=len("repositories")    
for key in suite_spec:
  if key == "name":
    suite_name= suite_spec[key]
    
    # - - - - - - - - - - - - - - - - - - - - - - - - 
    suite_dir        = os.path.join( suites_dir, suite_name)
    
    repositories_dir = os.path.join( suite_dir, "repositories")
    worktrees_dir    = os.path.join( suite_dir, "worktrees")
    tasks_dir        = os.path.join( suite_dir, "tasks")
    
#
    make_folders(repositories_dir)
    make_folders(tasks_dir)
    make_folders(worktrees_dir)
#    make_folders(logs_dir)
#    make_folders(builds_dir)
#    make_folders(installs_dir)
    # - - - - - - - - - - - - - - - - - - - - - - - - 
  if key == "repositories":
    repositories = suite_spec[key]
  if key == "tasks":
    tasks = suite_spec[key]
  
logs.log_labeled( "Suites", suite_dir, label_len, 1) 
logs.log_labeled( "Repositories", repositories_dir, label_len, 0) 
logs.log_labeled( "Worktrees", worktrees_dir, label_len, 0) 
    
logs.log_labeled( "Tasks", tasks_dir, label_len, 0) 
#logs.log_labeled( "Builds", builds_dir, label_len, 0) 
#logs.log_labeled( "Installs", installs_dir, label_len, 0) 
#logs.log_labeled( "Packages", packages_dir, label_len, 0) 

#logs.log_labeled( "Logs", logs_dir, label_len, 0) 

for repo in repositories:
    repo_name        = repo.get("name")
    repo_type        = repo.get("type")
    repo_main_branch = repo.get("main-branch")
    repo_initial_branch = repo.get("initial-branch")
    repo_origin      = repo.get("origin")
    repo_upstream    = repo.get("upstream")
    repo_search      = repo.get("search")
# - - - - - - - - - - - - - - - - - - - -
# At this point in the repository loop, we know enough to create 
# or verify a repository.  
# We are doing one of three opertions to create
# a repository:
#   copy
#   git-init
#   git-clone
# 
#   After the repository is created, cloned or copied
#   the main-branch, if given will be checked out
#   in the repository directory
# 
    if repo_search != "":
      repo_copy_path = find_repository_to_copy(repo_name,repo_search)
    
    repo_path=os.path.join(repositories_dir,repo_name+".git" )

    if repo_copy_path  != "":
        repo_type = "copy" # overrides git-int and git-clone if a repo with the same name was found
    if repo_type == "copy":
      copy_repo( repositories_dir, repo_copy_path, repo_path)
    if repo_type == "git-clone":
      clone_repo(repositories_dir, os.path.join(repositories_dir,repo_name+".git"), repo_name, repo_main_branch, repo_origin, repo_upstream)
    if repo_type == "git-init":
      git_init(repositories_dir, repo_name, repo_initial_branch)
        
for task in tasks:
  # - - - - - - - - - - - - - - - - - - - - - - 
  # Create task, build, install and logs subdirectories for this task

  task_name = task['name']
  task_path = os.path.join(tasks_dir, task_name)
  #builds_path = os.path.join(builds_dir, task_name) 
  #installs_path = os.path.join(installs_dir, task_name) 
  #log_path = os.path.join(logs_dir, task_name) 
  make_folders(task_path)
  #make_folders(builds_path)
  #make_folders(installs_path)
  #make_folders(log_path)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # create symlinks for building, installing and logging.
  #build_symlink_path=os.path.join(task_path,'build')
  #install_symlink_path=os.path.join(task_path,'install')
  #log_symlink_path=os.path.join(task_path,'logs')
  #create_symlink(builds_path,build_symlink_path)
  #create_symlink(installs_path,install_symlink_path)
  #create_symlink(log_path,log_symlink_path)
 
  # - - - - - - - - - - - - - - - - - - - - - - 
  # Construct the contents of a .code-workspace file for the task
  # Part 1 - the beginning
  #
  task_code_workspace='''{ 
	  "folders": [
		{
			"path": "./.vscode"
		},{
      "tools": "toolkit"
      },
		{
			"path": "build"
		},
		{
			"path": "install"
		}
	]
}'''
  task_worktrees = task['worktrees']
  
  for task_worktree in task_worktrees:
      repository_name = task_worktree['repository']
      
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
      branch=task_worktree['branch']
      task_worktree_path=os.path.join(task_path, repository_name)
      worktree_path=os.path.join(os.path.join(worktrees_dir,branch),repository_name)
      #build_path=os.path.join(os.path.join(builds_dir,branch),repository_name)
      #;install_path=os.path.join(os.path.join(installs_dir,branch),repository_name)
      # This is commented out for now in favor of putting symlinks in the 
      # task folder.
      # # Construct the contents of a .code-workspace file for the task
      # # Part 2 - the path to each worktree
      # #
      # task_code_workspace += ''',{
      #   "path": "''' + worktree_path + '''"
      #   }'''
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      # the same worktree of a repository may be used for multiple 
      # tasks.
      #
      # for each task's list of repositories, 
      # create the worktree for the branch and repository
      # if one has not already been created for another task

      chdir(os.path.join(repositories_dir,repository_name+".git"))
      if not os.path.isdir(worktree_path):
        create_branch(repositories_dir, repository_name, branch)
        create_worktree( repositories_dir, repository_name, branch, worktree_path)
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      # create a symlink to the worktree in the task directory
      #
      chdir(os.path.join(tasks_dir,task_name))
      worktree_symlink_path=os.path.join(task_path,repository_name)
      create_symlink(worktree_path,worktree_symlink_path)
      
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Write the .code-workspace file if one does not exist
  task_code_workspace_file= os.path.join(task_path,task_name+".code-workspace")
  if not os.path.exists( task_code_workspace_file 
     or suite_spec['recreate-code-workspaces'] == "true"):
    with open(task_code_workspace_file, 'w') as f:
        f.write(task_code_workspace)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  
  