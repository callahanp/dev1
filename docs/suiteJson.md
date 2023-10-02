# Suite Json File 

## "suite-name": "prefix-app-name-suffix>

  Suite names should have something to distinguish them from similarly named repositories.
  This will avoid paths of the form ../name-1/worktrees/name-1/src which could be confusing

  A prefix or suffix indicating that the directory is a DEV1 suite is recommended but not required.
  Suffix _s or s_ is sufficient. _suite or suite_ is also sufficient but more typing.

## "repositories": []

An array whose elements describe a group of repositories.  These can be clones of other repositories or newly created repositories iwht no origin or upstream specified.

  Repository tags include:

  "name":
  "create-method": one of "clone", "git-init", "copy"
  "main-branch":   the main branch of ongoing development
  "origin":        the origin URL
  "upstream":      the origin URL

 A set of search paths for repositories can be specificed on the command line.  If the create method is clone, bootstrap will search the paths by name for a repository with the given orgin or upstream and copy it instead of cloning.

 You should only need one copy of a repository. Git worktrees will be used for working on different branches or tags.

 You should explicity specify any repository that must be built for any reason.  If you have a given library or development tool installed system wide, it does not need a repository specified unless you need a specific version not available through a standard system install.

## Tasks:

Tasks are created for any bit of work that requires specific commits, branches or tags from a set of repositories. An abbreviation of a branch, tag, or description of the work to be done can be used as the "task-name"

Tasks are represented in json as a name and a list of repositories and their respective branches 

"Tasks": [
    "name": "next",
    "worktrees": [{
      "repository-name":  "flightgear",
      "branch":           "next"
      },{
      "repository-name":  "simgear",
      "branch":           "next"
      },{
      "repository-name":  "fgdata",
      "branch":           "next",
      "symlink-location": "installs/task-name/flightgear"
      },{
      "repository-name":  "fgmeta",
      "branch":           "next"
      },{
      "repository-name":  "osg",
      "branch":           "OpenSceneGraph-3.6"
    }]
]

Note that four of the repositories share the same branch.  "next" is the ongoing development branch for FlightGear.

A task for a bug-fix might affect only one repository
  {
    "name": "bf4217",
    "worktrees": [{
      "repository-name":  "flightgear",
      "branch":           "Bugfix - Issue 4217 - Subscriptions"
      },{
      "repository-name":  "simgear",
      "branch":           "next"

      (same as above)
      }]
  }

Because multiple tasks can require the same worktree, the task directories contain a symbolic link to the actual task directory.  Any Integrated development environment or build tool will work against the Task Directory, either using the links, or the worktrees path directly in their configurations.

Because the links are full paths, moving anything at a high level, say to a new disk drive or changing DEV1_suites will require re-linking 