# DEV1 Folders

DEV1 organizes materials for an application or application suite in six folders.

application suite by organizing development materials in six folders within the containing folder for an application suite.

- Tasks, one or more, like bug-fix-42 or release-2020.4.1
- Repository, one or more repositories per suite
- Worktrees, one per repository branch
- Builds, one per task
- Installs, one per task
- Packages, one per task
- Logs, one folder per task

These are the actual names used for these folders.  A future version may allow you to assign your own names for each suite.

## tasks

Tasks set the task for a specific bit of work. They're responsible for creating maintaing, and using repository branches, worktrees, builds, installs and packages.

## repositories

Repositories contains clones of forks or original repositories.  Repositories for forks can have an upstream assigned, either the official repository, or if working as part of a team, the team's fork.  Only one copy of a repository is needed regardless of how many tasks are present.

## worktrees

Worktrees contain git worktrees created for tasks.  A task may use one branch name on one or more repositories.  Other repositories may require a specific branch or tag to support the task.  Tasks are not branches.  They're a whole set of branches, one per repository needed for the task.

## build

The build folder for a repository on a specific branch needs its own folder.  Task folder names are repeated in the Build folder for this purpose.  Inside the Build/Task folder you'll find a folder for each repository to be built.  The builds are done using these folders for out-of-tree builds.

$DEV1_APPS/{app}/{build}/{task}/{repository-name}

## install

Installation files ready for use are placed here. The folder scheme is similar to builds.

$DEV1_APPS/{app}/{install}/{task-name}/{repository-name}

## package

Target directories for any release packaging work are here, again the same folder scheme:

$DEV1_APPS/{app}/{package}/{task-name}/{repository-name}

## logs

Logs for tasks attach to the task level so the repository-name is not part of the path. Logs for any step accomplished through DEV1 aliases include timing information provided the step is allowed to exit normally.

$DEV1_APPS/{app}/{logs}/{task-name}build.log
$DEV1_APPS/{app}/{logs}/{task-name}run.log
$DEV1_APPS/{app}/{logs}/{task-name}debug.log
$DEV1_APPS/{app}/{logs}/{task-name}debug.log
etc.

In summary, DEV0 provides standard location folders for source code and scripting and populates them with the materials needed for development.  You provide scripts and dev0 will call them using aliased commands, so the commands are similar between applications.  For more information on commands see README-Commands.md


