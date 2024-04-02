# DEV1 Commands 

DEV1 commands take two sets of parameters separated by --:

- context
- command-related

Context parameters include suite-name task-name & CodeWorkspace-name
Command-related parameters are passed to scripts that perform one of the folling actions:

- c or context <suite-name> <task-name> <CodeWorkspace-name>
- add-repo <suite-name> -- <repo-url> <local-repo-name> <initial-branch>
- add-worktree <suite-name> -- <local-repo-name> <branch-tag-or-commit> 
- add-task   [[<suite-name>] <task-name>] -- <local-repo-name> <branch-tag-or-commit> <build-type> [<task-name>]
- i or ide   [ <suite-name> <task-name> ]
- b or build [ <suite-name> <task-name> ] -- [<build-sepecific-parameters>]
- r or run   [ <suite-name> <task-name> ] -- [<run-sepecific-parameters>]

build and run commands include a facility to add configurable parameters.  Users can create a standard set of parmeters for the suite, and for each task.

Future:
Parameter Configurations are found in

-$DEV1_TASK_DIR/build_param*.txt
-$DEV1_SUITE_DIR/build_param*.txt

-$DEV1_TASK_DIR/run_param*.txt
-$DEV1_SUITE_DIR/run_param*.txt

parameters obtained from the task location override similar parameters from the suite directory.


## Find and Execute 

The several of the native commands in dev0 are basically forwarders that find the appropriate script to run and pass along parameters to it.

For example the Dev0 run command will search the Dev0 task tree, the active worktree, the primary worktree for a script named run.sh, change to that script's folder and run it with any parameters remaining in $@.  

The build, install and debug scripts operate the same way, except in cases where there is no build.sh install.sh or debug.sh to be found.  In that case it will report that no script was found and make an attempt at a generic approach.  

For example, for a build, change directory to any that have CMakeLists.txt without a parent directory having one and just run CMake with the supplied paremeters running debug will run gdb for the last executable run under dev0's purview, again using any parameters provided. Sometimes that will actually work.  Sometimes you'll have to write a specific script to do what you actually want.

Command Aliases look like this:
alias run='f(){ source /work/suites/dev1/commands/run $@;unset -f f; }; f'

The alias creates a function f.  f runs a bash source command with any extra parameters
specified in $@, then deletes itself.  After creating f, f is run.
