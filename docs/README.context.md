# DEV1 Context

The context for using operational commands to run DEV1's ide, build and run commands can be a bit daunting.  Numerous git clones, worktrees, git branches, build variants, and directories to keep it all straight.  Having a consistent directory structure is central to DEV1's operation.

One needs easy ways to navigate between these directories, and to refer to them in scripts.  The directory structure would be daunting in a complex situation such as an app with separate git repositories for its libraries and each major component. 

Examining a case with a single git repository and just one branch, main, will give us a start. At the simplest, there is no upstream, just origin.  Our app is brand new and has no code to speak of, just a hello world, and it builds.

At the top level is an APP or Suites directory where all of our apps and suites of apps live.  At this level everything is a suite and the name of the top level directory must be "suites".  You'll need read/write permissions to suites.  You can place it anywhere.

In .bashrc,  you'll need:
export DEV1_SUITES_PATH=/work/suites
source $DEV1_SUITES_PATH/dev1/worktrees/next/dev1/dev1rc



We'll explore this app from it's inception as an idea, through creating a git repository on the network or locally, cloning it locally with DEV1 and then developing a new feature in a new branch. Along the way we'll examine the context variables DEV1 uses to place materials and organize operations.

## Step 1. Create the git repo and put a README.md in it.

README.MD
  Example 1. C++, hello.c++, gcc
  
  A simple example, one of a series of git repositories demonstrating the basics of working with application code in a robust way using DEV1.



