# DEV1 Commands

Dev1 commands list:

## Context

Context setting commands

- s or suite
- t or task
- w or workspace

Operational Commands

- i or ide
- b or build (may include installing)
- r or run
- suite-specific-commands

Context is about which directory tree and sub-trees we want to work with, and what we 
want to do there. So lets talk about trees and commands to get some work done.

Generally, the main tree is the one containing all materials for a suite of applications. Call it the Suite, or App tree
We might have quite a collection of these in a directory somewhere named Suites or Apps.

The sub trees include

- git repositories
- git worktrees
- a directory or tree with links to git worktrees for working on a particular commit, tag or branch
- builds and installs of variants for specific commits, tags or branches

The actual subtree structure is flexible and is covered in another readme.
TODO: write a readme about the sub-tree structures used by DEV1

There are two ways to set the context in Dev1.

- context commands
- operational commands

## Commands - getting the work done

Each of the context and operational commands accept parameters that specify the application materials to work with

- suite - which application, and optionally which branch and which code-workspace
- task - which branch and optionally which code-workspace
- workspace - which code-workspace
- ide - Which application, Which branch, which code-workspace
- build - Which application, Which branch, which variant, which targets, which set of options and parameters
- run - Which application, Which branch, which variant, which set of options and parameters

Flattening that out so we can handle and persist context:

- suite
- task
- workspace
- variant
- build-option-set
- run-option-set
- build-parameter-set lists of
- run-parameter-set

Build and run option or parameter sets might need explaining.  In Dev1, they are just small text files with lists of options and parameters that can be attached to build and run commands.

To make life easier, we want to be able to specify these things once and have the choice
remembered and not have to be re-typed when we repeat an operation. If I just enter run at the command line, whatever ran last time, runs again, with exactly the same options and parameters.

TODO make it so overriding options and parameters persists

If we open a new window and just use an operation without parameters, the context we were last using
should be set for the new window.  If we reboot, the existing sessions, and perhaps its windows and ides should re-open automatically

TODO Full implementation of window persistence

About the individual commands:

suite, task and workspace simply set environment variables and store persistence data
ide uses a .code-workspace configuration file if available and starts visual studio code code-insiders
build and run invoke shell scripts specific to the application or suite, with names "build*"" or "run*"" from the task or project folder. if opt* or param* files are present in the project folder, they will be applied to the corresponding run or build command. Parts of the filenames of run, options and parameter files are used to match which are used together.

example:
project/build_all
project/opt_all (optional)
project/param_all (optional)

These three imply an "all" target and the command "build all" would use all three files appropriately to build whichever variant was previously selected for whichever branch was previously selected.


