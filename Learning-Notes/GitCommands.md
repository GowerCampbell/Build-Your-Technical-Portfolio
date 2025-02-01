# Git Commands and Their Effects on Files

This document explains what each Git command does and how it affects the files. Use this as a quick reference guide for managing my Git workflow.

---

## **Setup & Initialization**

### `git init`
- **What it does**: Initializes a new Git repository in the current directory.
- **Effect on files**: Creates a hidden `.git` folder that stores all the metadata and version history for your project.

### `git clone <url>`
- **What it does**: Copies an existing remote repository (e.g., from GitHub) to your local machine.
- **Effect on files**: Downloads all files and the entire commit history from the remote repository to your working directory.

---

## **Staging & Snapshot**

### `git status`
- **What it does**: Shows the current state of your working directory and staging area.
- **Effect on files**: Lists which files are:
  - **Untracked**: Not yet added to Git.
  - **Modified**: Changed but not staged.
  - **Staged**: Ready to be committed.

### `git add <file>`
- **What it does**: Adds a file (or changes in a file) to the staging area.
- **Effect on files**: Moves the file from the **working directory** to the **staging area**, preparing it for the next commit.

### `git reset <file>`
- **What it does**: Removes a file from the staging area.
- **Effect on files**: Moves the file back to the **working directory**, but keeps the changes intact.

### `git diff`
- **What it does**: Shows the differences between the working directory and the staging area.
- **Effect on files**: Highlights changes that are not yet staged for commit.

### `git diff --staged`
- **What it does**: Shows the differences between the staging area and the last commit.
- **Effect on files**: Highlights changes that are staged but not yet committed.

### `git commit -m "message"`
- **What it does**: Creates a new commit with the changes in the staging area.
- **Effect on files**: Saves a snapshot of the staged files in the Git repository. The working directory is now clean (no uncommitted changes).

---

## **Branching & Merging**

### `git branch`
- **What it does**: Lists all branches in the repository.
- **Effect on files**: Shows which branch you are currently on (marked with an asterisk `*`).

### `git branch <branch-name>`
- **What it does**: Creates a new branch.
- **Effect on files**: Creates a new pointer to the current commit but does not switch to the new branch.

### `git checkout <branch>`
- **What it does**: Switches to the specified branch.
- **Effect on files**: Updates the working directory to reflect the state of the files in the selected branch.

### `git checkout -b <branch-name>`
- **What it does**: Creates a new branch and switches to it.
- **Effect on files**: Combines `git branch <branch-name>` and `git checkout <branch-name>`.

### `git merge <branch>`
- **What it does**: Merges the specified branch into the current branch.
- **Effect on files**: Combines changes from both branches. If there are conflicts, Git will prompt you to resolve them.

---

## **Inspecting & Comparing**

### `git log`
- **What it does**: Displays the commit history for the current branch.
- **Effect on files**: Shows a list of commits, including commit hashes, authors, dates, and messages.

### `git log --pretty=oneline`
- **What it does**: Displays the commit history in a concise, one-line format.
- **Effect on files**: Shows a simplified view of the commit history.

### `git diff <branchA>..<branchB>`
- **What it does**: Shows the differences between two branches.
- **Effect on files**: Highlights changes in `branchB` that are not in `branchA`.

### `git show <commit>`
- **What it does**: Displays details about a specific commit.
- **Effect on files**: Shows the changes made in that commit.

---

## **Sharing & Updating**

### `git remote add <alias> <url>`
- **What it does**: Adds a remote repository (e.g., GitHub) as an alias.
- **Effect on files**: Links your local repository to a remote one, allowing you to push and pull changes.

### `git fetch <alias>`
- **What it does**: Downloads changes from the remote repository but does not merge them.
- **Effect on files**: Updates your local repository with the latest changes from the remote, but leaves your working directory unchanged.

### `git push <alias> <branch>`
- **What it does**: Uploads local commits to the remote repository.
- **Effect on files**: Updates the remote repository with your local changes.

### `git pull`
- **What it does**: Fetches changes from the remote repository and merges them into the current branch.
- **Effect on files**: Updates your working directory with the latest changes from the remote repository.

---

## **Temporary Commits**

### `git stash`
- **What it does**: Temporarily saves changes in the working directory.
- **Effect on files**: Moves uncommitted changes to a "stash" so you can switch branches or perform other tasks.

### `git stash pop`
- **What it does**: Restores the most recently stashed changes.
- **Effect on files**: Reapplies the stashed changes to the working directory and removes them from the stash.

### `git stash apply`
- **What it does**: Restores stashed changes but keeps them in the stash.
- **Effect on files**: Reapplies the stashed changes to the working directory without removing them from the stash.

---

## **Rewriting History**

### `git rebase <branch>`
- **What it does**: Reapplies commits from the current branch onto another branch.
- **Effect on files**: Creates a linear history by moving commits to the tip of the specified branch.

### `git reset --hard <commit>`
- **What it does**: Resets the working directory and staging area to match a specific commit.
- **Effect on files**: Discards all changes after the specified commit, so use with caution.

---

## **Ignoring Files**

### `.gitignore`
- **What it does**: Specifies files and directories that Git should ignore.
- **Effect on files**: Prevents untracked files (e.g., logs, build files) from being added to the repository.

---

## **Deleting & Moving Files**

### `git rm <file>`
- **What it does**: Removes a file from the working directory and stages the deletion.
- **Effect on files**: Deletes the file and marks it for removal in the next commit.

### `git mv <old-path> <new-path>`
- **What it does**: Moves or renames a file.
- **Effect on files**: Stages the move/rename operation for the next commit.

---

## **Final Notes**
- Git commands manipulate files in three main areas: the **working directory**, the **staging area**, and the **repository**.
- Use `git status` frequently to understand the state of your files.
- Always commit or stash changes before switching branches to avoid losing work.

---

Save this file as `GitCommands.md` in your repository for easy reference. Let me know if you need further assistance! 😊
