# Building My Brand - Technical Portfolio
# - Formulating career goals
# - Collaboration
# - Storing/restoring versions

# Git Components:
# The Working Directory
# Staging Area
# Git Repository

# In Git, your files have three main states:
# Committed, modified, and staged.

# Modify a file from a working directory
# Add these modified files to the staging area
# Perform a commit operation from the staging area and store
# in the Git Repository (database where your version control stores all
# the files for a particular project)

# Sharing code that can demonstrate my newly acquired skills
# to peers, potential clients, and employers.

# Types of repositories:
# Local (network) & Remote (such as GitHub) repositories.

# Local repositories:
# Initializing a repository:
# Git init (Subdirectory in my project)

# git add (add new files to my projects)
# /Users/user/your_repository git add newfile.py
# Using cd to locate a file

# Files can either exist in a tracked state or in an untracked state in my
# working directory. Tracked files are files that were in the last snapshot.
# Untracked files are any files in my working directory.

# git status
# Determines which files are in which state.

# git status
# on branch master
# your branch is up-to-date with origin/master'
# changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)

# Committing my changes
# You need to run 'git add' on the files that I have edited

# git commit
# Is a wrapper for a set of changes.
# Every set of changes creates a new, different version of my project
# '-m' allows me to leave a message in the files I have committed to the repository.

# git log
# Allows me to see the list of changes in reverse chronological order
# The git log command displays the commit hash (unique ID for a particular
# commit).

# git log
# commit actrtyfiuhiuy777ghiu77g77tgu779g7
# Author: HyperionDev <gower.campbell@gmail.com>
# Initial commit.

# Commands that allow you to customize or filter --pretty
# The oneline option is prebuilt options in conjunction with --pretty
# This option displays the commit hash and commit message on a single line
# git log --pretty=oneline:
# git log --pretty=oneline 14547517rtyr76r6rf7f887 Initial Commit

# Authenticating Git with your GitHub credentials
# Synchronize your local repository with a remote repository hosted by GitHub
# Using the GitHub Command Line Interface (GH CLI)

# Offers a range of features, for this task and academic program,
# we will only focus on installation and authentication.

# Skipping some steps downloading gh and logging in and choosing GitHub
# Authentication is completed.

# Syncing Your Local & Remote Repositories
# Create & add files to the local Git repository
# "push an existing repository from the command line:"

# Example:
# git remote add origin https://github.com/GowerCampbell/Cormacc_Hub.git

# SetUp
# git config --global user.name "[Gower Campbell]"
# git config --global user.email "[Gower.Campbell@gmail.com]"
# git config --global color.ui auto

# SetUp & INIT
# git init
# Initialize an existing directory (folder) as a Git Repository
# git clone [url]
# Retrieve an entire repository from a hosted location via URL

# Stage & Snapshot
# git status
# Show modified files in working directory for your next commit
# git add [file]
# Add a file as it looks now to your next commit stage
# git reset [file]
# Unstage a file while retaining the changes in working directory
# git diff
# Diff of what is changed but not staged
# git diff --staged
# Diff of what is staged but not yet committed
# git commit -m "[descriptive message]"
# Commit your staged content as a new commit snapshot

# Branch & Merge
# git branch
# List your branches. A * will appear next to the currently active branch
# git branch [branch-name]
# Create a new branch at the current commit
# git checkout
# Switch to another branch and check it out into your working directory
# git merge [branch]
# Merge the specified branch's history into the current one
# git log
# Show all commits in the current branch's history

# Inspect & Compare
# git log
# Show commit history for the currently active branch
# git log branchB...branchA
# Show the commits on branchA that are not on branchB
# git log --follow [file]
# Show the commits that changed file, even across renames
# git diff branchB...branchA
# Show the diff of what is in branchA that is not in branchB
# git show
# Show any object in Git in human-readable format

# Share & Update
# git remote add [alias] [url]
# Add a Git URL as an alias
# git fetch [alias]
# Fetch down all the branches from that Git remote
# git merge [alias]/[branch]
# git push [alias] [branch]
# Transmit local branch commits to the remote repository branch
# git pull
# Fetch and merge any commits from the tracking remote branch

# Tracking Path Changes
# git rm [files]
# Delete the file from the project and stage the removal for commit
# git mv [existing-path] [new-path]
# Change an existing file path and stage the move
# git log --stat -M
# Show all commit logs with an indication of any paths that moved

# Rewrite History
# git rebase [branch]
# Applies any commits of the current branch to the specified one
# git reset --hard [commit]
# Clear staging area, rewrite working tree from the specified commit

# Temporary Commits
# Temporarily store modified, tracked files in order to change branches

# git stash
# Save modified and staged changes
# git stash list
# List stack-order of stashed file changes
# git stash pop
# Write working from the top of the stash stack
# git stash drop
# Discard the changes from the top of the stash stack

# Ignoring Patterns
# Preventing unintentional staging or committing of files

# logs/
# *.notes
# pattern*/
# Save a file with desired patterns as .gitignore with direct string matches
# or wildcard globs.
# git config --global core.excludesfile [file]
# System-wide ignore pattern for all local repositories

# Branching (different versions of the codebase)
# Share and work on the same code (independent line of development)
# Mainline
# You create a new branch whenever you are working on a new feature or bug
# fixes (ensures unstable code is not committed) before merging it back

# Git Master branch when you make your first commit in the repository
# Until you make a new branch and switch over it.
# All following commits will go under the master branch.

# HEAD is used by Git to represent the current position of the branch.
# By HEAD will be a new repository and changing where the HEAD is pointing will
# update the my current branch.

# Check on 'git status' in the first line of output.
# git branch my-first-branch (creating a branch)

# Switching branches
# git checkout my-first-branch (Switch to a new branch)
# Using this will take the HEAD to my-first-branch
# git checkout -b my-second-branch (short for git branch/checkout)

# Saving changes temporarily
# Using Commit, you save your changes permanently in the repository.
# Ensure you can switch between your branches and the master branch
# Making sure you have no uncommitted changes as Git will not let you switch
# branches before using 'git stash' command (clean working slate)

# Using git stash
# Takes all the changes in your working copy and saves them on a clipboard
# Letting you restore changes from the clipboard in your working copy
# To restore your saved stash and clear it
# git stash pop
# Get a specified stash but keep it saved on the clipboard
# git stash apply <stashname>

# Merging (git merge)
# Independent lines and from a Git branch and integrate into a single branch
# git checkout master
# git merge my-first-branch

# Updated default branch name from 'master' to 'main'

# Cloning a repo to quick start
# As a software engineer, tasked with closing one or more issues on a
# specific repository.
# Remember git clone https://github.com/[username]/[repo].git

# Plain-English description is important for the bug fix, performance
# improvement, or a new feature. (Helps the line manager know what's done)

# Working on your own Branch
# With your co-worker's code to ensure that it's a branch
# give it proper names like:
# git checkout -b issue-1
#
# Leave behind messages
# git commit -m "changed program to use driver-inf.txt"
# git push origin issue-1

# Making a pull request
# Pull Request (PR) is a request asking that your branch be merged with the master
# branch to be part of the main code base. It is my responsibility to give them
# my coded changes to review.

# Code Review
# Uses your pull request with the attached changes and shows what you have
# done. Make sure to add comments as the reviewer will be able to see
# 'diff'erent the developer can now make requested fixes and commit and push
# them to the PR automatically. Once pushed, you can review changes.

# Finally Merging
# Head to your PR on GitHub, click on conversations and go to "merge pull
# request" (After the successful building and passing of tests)
# Leave your closing remarks (PR #2 closed this issue.)
# "Close and comment"
# Changes reflected in your computer:
# git checkout master
# git pull origin master

# GitHub and my Developer Portfolio (collection of online programs you have
# developed) industry-recognized. Use my experience with Git and GitHub.

# README.md files (essential for all software projects)
# Describe your code. Tell the reader what the project does and why it is
# useful, who maintains and contributes to the project, and how a user can get
# your code to work.

# Project Name
# Description of project (importance and what it does)
# Table of contents that allows people to navigate
# An installation section (how to install the project locally)
# A usage section that instructs others how to use my project after
# they have installed it (include screenshots of your project in action)
# ---push these images into my repository.
# A section for credits, which highlights and links authors of your project.

# README has a .md which stands for Markdown. Markdown is a syntax that
# lets you style text. If you write a program like MS Word, using a toolbar to
# select appropriate options to style my text (e.g., certain text bold,
# underlined, or formatted). For example, keywords and characters like "* *"
# to italicize text.

# Markdown syntax taken from the GitHub guide

# Headers
# "#" using hash symbols to represent H1 (Main Titles)
# "##" using hash symbols to represent H2 (Subtitles)
# "######" using hash symbols to represent H6 (smallest heading)

# Emphasis
# *This text will be italic*
# _This will also be italic_
# **This text will be bold**
# __This will also be bold__
# _You **can** combine them_

# Unordered lists
# * Item 1
# * Item 2
#   * Item 2a
#   * Item 2b

# Ordered Lists
# 1. Item 1
# 2. Item 2
# 3. Item 3
#   a. Item 3a
#   b. Item 3b

# Images
# ![alt text](image url)
# Example: ![GitHub Logo](/images/logo.png)

# Links
# [link text](link url)
# Example: [GitHub](http://github.com)
# OR use a shortcut
# <link>

# Blockquotes
# > This is a block quote. It can span multiple lines.
# It will display the quote with a grey line on the left-hand side
