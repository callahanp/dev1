# DEV1 Context

The context for using operational commands to run DEV1's ide, build and run commands can be a bit daunting.  Numerous git clones, worktrees, git branches, build variants, and directories to keep it all straight.  Having a consistent directory structure is central to DEV1's operation.

One needs easy ways to navigate between these directories, and to refer to them in scripts.  If you are used to working in a single set of directories by using git stash, it will take some getting used to.  Instead of one place to go to work on an app, you now have as many as you have different tasks.

Examining a case with a single git repository and just one branch, main, will give us a start. At the simplest, there is no upstream, just origin.  Our app is brand new and has no code to speak of, just a hello world, and it builds.

Above, at the top level is an APP or Suites directory where all of our apps and suites of apps live. The name of the top level directory must be "suites".  You'll need read/write permissions to suites.  You can place it anywhere.

In .bashrc,  you'll need:

export DEV1_SUITES_PATH=/work/suites
source $DEV1_SUITES_PATH/dev1/worktrees/next/dev1/dev1rc

