
root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane fraud-detection on  master ➜  git branches -a
git: 'branches' is not a git command. See 'git --help'.

root@controlplane fraud-detection on  master ✖ init dvc
Expected single character argument.

root@controlplane fraud-detection on  master ✖ dvc
ERROR: the following arguments are required: command
usage: dvc [-q | -v] [-h] [-V] [--cd <path>] [--wait-for-lock]
           command ...

Data Version Control

options:
  -q, --quiet        Be quiet.
  -v, --verbose      Be verbose.
  -h, --help         Show this help message and exit.
  -V, --version      Show program's version.
  --cd <path>        Change to directory before executing.
  --wait-for-lock    Wait for the lock if it is already held by another process, instead of failing immediately.

Available Commands:
  command            Use `dvc command --help` for command-specific help.
    add              Track data files or directories with DVC.
    artifacts        DVC model registry artifact commands.
    cache            Manage cache settings.
    check-ignore     Check whether files or directories are excluded due to `.dvcignore`.
    checkout         Checkout data files from cache.
    commit           Record changes to files or directories tracked by DVC by storing the current versions in the cache.
    completion       Generate shell tab completion.
    config           Get or set config options.
    dag              Visualize DVC project DAG.
    data             Commands related to data management.
    pull             Download tracked files or directories from remote storage.
    push             Upload tracked files or directories to remote storage.
    fetch            Download files or directories from remote storage to the cache.
    status           Show changed stages, compare local cache and a remote storage.
    destroy          Remove DVC files, local DVC config and data cache.
    diff             Show added, modified, or deleted data between commits in the DVC repository, or between a commit and the workspace.
    du               Show disk usage.
    experiments (exp)
                     Commands to run and compare experiments.
    freeze           Freeze stages or .dvc files.
    unfreeze         Unfreeze stages or .dvc files.
    gc               Garbage collect unused objects from cache or remote storage.
    get              Download file or directory tracked by DVC or by Git.
    get-url          Download or copy files from URL.
    import           Download file or directory tracked by DVC or by Git into the workspace, and track it.
    import-db        Snapshot a table or a SQL query result to a CSV/JSON format
    import-url       Download or copy file from URL and take it under DVC control.
    init             Initialize DVC repository.
    install          Install DVC git hooks into the repository.
    list (ls)        List repository contents, including files and directories tracked by DVC and by Git.
    list-url (ls-url)
                     List directory contents from URL.
    metrics          Commands to display and compare metrics.
    move (mv)        Rename or move a DVC controlled data file or a directory.
    params           Commands to display params.
    plots            Commands to visualize and compare plot data.
    queue            Commands to manage experiments queue.
    remote           Set up and manage data remotes.
    remove (rm)      Remove stages from dvc.yaml and/or stop tracking files or directories.
    repro            Reproduce complete or partial pipelines by executing their stages.
    root             Return the relative path to the root of the DVC project.
    stage            Commands to list and create stages.
    studio           Commands to authenticate DVC with Iterative Studio
    unprotect        Unprotect tracked files or directories (when hardlinks or symlinks have been enabled with `dvc config cache.type`).
    update           Update data artifact imported (via dvc import or dvc import-url) from an external DVC repository or URL.
    version (doctor)
                     Display the DVC version and system/environment information.

root@controlplane fraud-detection on  master ✖ dvc init
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/treeverse/dvc>

root@controlplane fraud-detection on  master [+] ➜  git add .

root@controlplane fraud-detection on  master [+] ➜  git commit -m "Initialize DVC"
[master 6b37f7e] Initialize DVC
 3 files changed, 6 insertions(+)
 create mode 100644 .dvc/.gitignore
 create mode 100644 .dvc/config
 create mode 100644 .dvcignore

root@controlplane fraud-detection on  master ➜  
