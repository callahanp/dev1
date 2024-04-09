# DEV1 Commands

Dev1 is quite capable of managing a complex and dynamic development environment containing multiple application and library repositories, both personal forks and upstream.  It supports these with the usual development activities across branches, tags, specific commits, specific build variants and sets of environment variables and run time options.

Features:
    - Multiple Libraries
    - Multiple Applications
    - Personal Forks
    - Clones of Personal Forks or Upstream repositories for the same repository
    - Clones are done with git clone --bare.  Git worktrees are created for any required commit, tag or branc
    - Pull from upstream, push to origin (fork) or push and pull from origin
    - ssh access to remote repositories (SourceForge, GitLab, GitHub)
    - Only one copy of a given worktree is needed to support source editing and building
    - Symbolic links to worktrees used for code workspaces and builds
    - JSON configuration file
    - Git commits, tags and branches organzized as separate tasks with connections to requred worktrees
    - Multiple Code workspaces with selected Git Worktrees for each Task are possible
    - Separate source and build directories for multiple variants for selected git commits, tags or branches

DEV1 includes wrapper commands on individual project's take on three processes:

- starting visual studio code
- building using a custom script for the project
- running software

The wrappers are aliased in dev1rc as functions that will source the corresponding dev1 command.

- i and ide - This typicaly starts visual studio code
- b and build - run project build scripts
- r and run - run scripts that run specific executables

These aliases can be used from any directory and must in that case specify a context.
Context information that must be supplied varies between the three commands but is used to specify

- the suite
- the task, usually a particular git reference.  In other words, a git commit, tag or branch.
- which build variant should be built or run
- which of several run scripts to run
- which of several .code-workspace files to use with code or code-insiders

devrc is aliased to run itself

take two sets of parameters separated by --:

- context
- command-related

Context parameters include suite-name task-name codeWorkspace-name & build-variant. They can be in any order
Context parameters are optional, and if not provided will be populated from

- The current directory's path
- The previous supplied value

Context parameters will be checked against the project's directory structure to ensure they are valid, and unique.

Command-related parameters are passed to scripts that perform one of the folling actions:

- s or suite   suite-name task-name codeWorkspace-name build-variant
- i or ide     suite-name task-name codeWorkspace-name
- b or build   suite-name task-name build-variant -- [build-sepecific-parameters]
- r or run     suite-name task-name  -- [run-sepecific-parameters]

build and run commands include a facility to add configurable parameters.  Users can create a standard set of parmeters for the suite, and for each task.
