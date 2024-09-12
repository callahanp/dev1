# DEV1  A Simple Robust Development Environment for the rest of us

## Cautions

### DEV1 was alpha software

DEV1 is replaced by DEV0, a minimalist implementation of the ideas covered by DEV1

DEV0 is much simpler and emphasizes  the dev0 commands, ide, build and run. 
It includes examples of user-provided implementation scripts for building and running executables that are part of the application.

More information on DEV0 can be found at: https://github.com/callahanp/dev0

DEV1 will be removed from github by Dec 31, 2024

DEV1 is fully obsolete and should not be used for new development.
A utility is in the works for converting a DEV1 suite to a DEV0 suite.

You can use DEV1 alongside what you usually use in a separate directory.

### DEV1's commands and configuration are subject to change without notice

### The next and main branches are stale. Use tickets/0001 for now

### There are no releases, not even 0.1  Alpha Release 0.1 planned for early June 2024

## The good news

The 0001 branch works even if it is not feature-complete.

DEV1 provides a simple user interface for managing complex open-source development activity.

It organizes project materials and provides simplified development commands across different projects.  The commands cover most of the steps a developer takes every working day.  It allows rapid context switching between different build types for specific branches, tags, or commits, delivering changes via personal forks of upstream repositories.  Dev1 avoids using git stash, preferring separate worktrees for different contexts.

Open-source developers of one organization frequently contribute changes to supporting libraries or data sources.  DEV1 allows such work under the same suite as the main application. DEV1's workspaces can include repositories and worktrees from multiple organizations, simplifying coordination.

Application Suite Development Activities include formal versions, specific new features, or bug fixes.  Usually, only one or a few repositories in the suite of application and library builds need a different branch, while others remain on a release branch.

Keeping all that straight with multiple bugfix branches, feature branches, and maintained releases can be daunting.  DEV1 provides a way to manage it.

DEV1 uses Visual Studio Code workspaces, git bare repositories, and git worktrees to organize materials for a suite.

A suite directory contains the source repository materials and additional data, scripts, and programs needed to build components of an application suite.
For example, FlightGear's development suite in /suites/fg/tasks/next

For example, FlightGear uses the OpenSceneGraph library, among others.  DEV1 can add tool and library repositories and relevant branch worktrees to build and take advantage of un-released features and remove them once released.

DEV1 optionally supports independent builds for dependencies, treating their code and repositories the same as any other part of the application.

## Overview

Work on an application suite may include bug fixes, new features, refactoring, and release maintenance. Simultaneous work on more than one of these requires separate worktrees.  Dev1 directly supports this with git worktrees.

DEV1 supports an application suite by organizing development materials in five folders.

- Project" DEV1 configuration file, build and run scripts, .git-exclude
- Repositories: one or more bare git repositories per suite
- Worktrees: For each repository, with branches you will be working with, there will be one git worktree per branch.
- Builds: One folder for each repository and branch required for a task, containing symbolic links to corresponding worktrees
- Tasks: one or more, usually named for specific branches or tags, like bug-fix-42 or release-2020.4.1 Contains a multi-root.code-workspace file

Each "task" directory contains

- a code-workspace file
- links to each worktree for the specific branches of repositories needed for the task
- parameter snippets for builds, debugging, and running commands

DEV1 does not decide how things should be built, installed, run, or packaged. Scripts you've already written provide that.  Dev1 provides aliases to call your scripts with specific sets of parameters. These aliases are  the same across different suites:

- s or suite: set the suite,task, code-workspace file and CMake Build Type
- t or task: to set the task for the current suite
- i or ide: start visual studio code for the current suite and task
- b or build: build
- r or run
- g or debug
- t or tests

DEV1 includes support only for VisualStudioCode. But it could quickly adapt to use any other IDE.
