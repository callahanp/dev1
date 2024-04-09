# Installing DEV1

## The current state of development of DEV1 itself

First, there is no installer or installable package, just a git repo.  Everything is under development so there is no main branch, just next.

TODO: DEV1 needs to be installable
TODO: DEV1 is known to work on Ubuntu Linux only

## Step 1:  Setup DEV1's main directory and dev1rc

Add to .bashrc to identify where DEV1 stores everything you need to work on applications need using DEV1's features and run dev1rc

~~~ bash
export DEV1_PARENT=/work
export DEV1_SUITES_PATH=/$DEV1_PARENT/suites
DEV1_RC=$DEV1_SUITES_PATH/dev1/worktrees/next/dev1/dev1rc
if [[ -e $DEV1_RC ]]; then source $DEV1_RC
~~~

## step 2:  run your bashrc

## step 3:  create the suites directory

~~~ bash
   mkdir -p $DEV1_SUITES/dev1/project
   touch $DEV1_SUITES/dev1/project/dev1.config.json
~~~

## step 4 : create a suite and project folder for dev1

~~~ bash
    cd $DEV1_SUITES/dev1
    code .
~~~

## Step 5: Edit the dev1.config.json file

~~~ json
{
  "config": { "repositories": [
         {
         "url": "https://@github.com/callahanp/dev1.git",
         "localRepositoryName": "dev1",
         }
      ]
  }
}
~~~
