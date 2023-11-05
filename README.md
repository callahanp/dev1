# DEV1  A Simple Robust Development Environment for the rest of us

DEV1 provides a simple user interface for managing complex open-source development activity.

It organizes project materials and provides simplified development commands across different projects. Open-source application suites and collections of libraries from a single organization might host several related repositories. Sometimes, work on an application suite includes working with repositories from other organizations.

Application Suite Development Activities include formal versions, specific new features, or bug fixes.  Usually, only one or a few repositories in the suite of application and library builds need a different branch, while others remain on a release branch.

Keeping all that straight with multiple bugfix branches, feature branches, and maintained releases can be daunting.  DEV1 provides a way to do it.

DEV1 uses Visual Studio Code workspaces, git bare repositories, git worktrees to organize materials for a suite.

A suite directory contains the source repository materials and additional data, scripts and programs needed to build components of an application suite. 
For example, FlightGear's development suite in /suites/fg

Open-source developers of one organization frequently contribute changes to supporting libraries or data sources.  DEV1 allows such work under the same suite as the main application.

For example, FlightGear uses the OpenSceneGraph library, among others.  At one time, Flightgear used next-release features of CMake, so for a brief period, CMake was treated as a build target in FlightGear's suite of executables and would have been treated as a part of the flightgear suite.

When a specific build of FlightGear requires a particular version of OpenSceneGraph or any other library or tool, DEV1 supports direct building what your tasks need.

DEV1 directly supports independent builds for such dependencies, treating their code and repositories the same as any other part of the application.
  
Work on an application suite may include bug fixes, new features, refactoring, and release maintenance. Simultaneous work on more than one of these requires separate worktrees.  Dev1 directly supports this with git worktrees.

DEV1 supports an application suite by organizing development materials in three folders.

- Repositories: one or more bare git repositories per suite
- Worktrees: one git worktree per branch of each repository
- Tasks: one or more, like bug-fix-42 or release-2020.4.1 

Each task directory contains 

- a code-workspace file
- links to each worktrees for the specific branches of repositories needed for the task 

The task directory may include links to a worktree of a repository used to hold scripts related to various development tasks

DEV1 does not decide how things should be built, installed, run, or packaged. Scripts you've already written provide that.  Dev1 provides aliases to call yours. These aliases are  the same across different suites:
- s or suite: set the suite and task
- t or task: to set the task for the current suite
- b or build: build
- r or run
- g or debug 

DEV1 includes support only for VisualStudioCode. But it could quickly adapt to use any other IDE.
