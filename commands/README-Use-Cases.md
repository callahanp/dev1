# DEV1 Use Cases

## Initial Usage

Bootstrapping DEV1

~~~ bash
# define a parent directory for application suites
cd top-level-dir
export DEV1_PARENT_PATH=$(pwd)
export DEV1_SUITES_PATH=$DEV1_PARENT/suites
DEV1_SUITES_PATH
mkdir -p dev1/project
~~~

Add to .bashrc, providing a base directory for a local projects,and usernames for github, gitlab, sourceforge.

~~~ bash
# DEV1
export DEV1_PARENT=[parent]
export DEV1_GITLAB_USERNAME=[gitlab-username]
export DEV1_GITHUB_USERNAME=[github-username]
export DEV1_SOURCEFORGE_USERNAME=[sourceforge-username]

export DEV1_SUITES_PATH=$DEV1_PARENT/suites

DEV1_RC=$DEV1_SUITES_PATH/dev1/worktrees/next/dev1/dev1rc

if [[ -e $DEV1_RC ]]; then source $DEV1_RC; fi

# DEV1 end
~~~

## Initialize New Project

A new project in DEV1 includes the following operations:

~~~ bash
suiteDir=$DEV1_SUITES_PATH/[New-App-or-Suite-Name]/
mkdir -p -mode=rw $suiteDir
cd $suiteDir
mkdir -p -mode=rw repositories worktrees tasks project run
git clone --bare  [repository-url-or-file]

~~~

## Activate Existing Branch

## Create New Branch

## Local Repository

## Remote Repository

## Make LocaL Repository a clone of a remote repository

<https://docs.github.com/en/github-cli/github-cli/about-github-cli>

<https://medium.com/@farzanajuthi08/how-to-make-a-project-into-gitlab-and-upload-your-existing-code-into-gitlab-e6ba60e81dcb>

<https://sourceforge.net/p/forge/documentation/Git/>

## Remote Fork
