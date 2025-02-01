# **Building My Brand - Technical Portfolio**

## **Career Goals**
- Formulate clear career goals.
- Collaborate effectively with peers, clients, and employers.
- Store and restore versions of your work using Git.

---

## **Git Components**
1. **Working Directory**: Where you make changes to files.
2. **Staging Area**: Where you prepare changes for committing.
3. **Git Repository**: The database where all versions of your project are stored.

---

## **File States in Git**
1. **Committed**: Files safely stored in the repository.
2. **Modified**: Files changed in the working directory but not committed.
3. **Staged**: Files marked to be included in the next commit.

---

## **Git Workflow**
1. Modify files in the **working directory**.
2. Add modified files to the **staging area** using `git add`.
3. Commit changes from the staging area to the **Git repository** using `git commit`.

---

## **Sharing Code**
- Use Git to share code that demonstrates your skills with peers, clients, and employers.
- Utilize **local** and **remote** repositories (e.g., GitHub).

---

## **Local Repositories**
1. **Initialize a Repository**:
   - Use `git init` to create a new Git repository in your project directory.
2. **Add Files**:
   - Use `git add <file>` to add new or modified files to the staging area.
3. **Tracked vs. Untracked Files**:
   - **Tracked**: Files in the last snapshot.
   - **Untracked**: Files not yet tracked by Git.
4. **Check Status**:
   - Use `git status` to see the state of your files.

---

## **Committing Changes**
1. Add files to the staging area with `git add`.
2. Commit changes with `git commit -m "commit message"`.
3. View commit history with `git log`.

---

## **Customizing Git Log**
- Use `git log --pretty=oneline` to display commit history in a concise format.

---

## **Syncing Local & Remote Repositories**
1. **Authenticate Git with GitHub**:
   - Use the GitHub CLI to log in and authenticate.
2. **Push to Remote Repository**:
   - Use `git remote add origin <repository-url>` to link your local repository to a remote one.
   - Push changes with `git push origin <branch>`.

---

## **Git Setup**
- Configure Git with your name and email:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  git config --global color.ui auto
  ```

---

## **Essential Git Commands**
### **Setup & Initialization**
- `git init`: Initialize a directory as a Git repository.
- `git clone <url>`: Clone a repository from a remote URL.

### **Staging & Snapshot**
- `git status`: Show modified files.
- `git add <file>`: Stage a file for commit.
- `git reset <file>`: Unstage a file.
- `git diff`: Show changes not yet staged.
- `git commit -m "message"`: Commit staged changes.

### **Branching & Merging**
- `git branch`: List branches.
- `git branch <branch-name>`: Create a new branch.
- `git checkout <branch>`: Switch to a branch.
- `git merge <branch>`: Merge a branch into the current one.

### **Inspecting & Comparing**
- `git log`: Show commit history.
- `git diff <branchA>..<branchB>`: Compare branches.

### **Sharing & Updating**
- `git remote add <alias> <url>`: Add a remote repository.
- `git push <alias> <branch>`: Push changes to a remote repository.
- `git pull`: Fetch and merge changes from a remote repository.

---

## **Branching**
- Create branches for new features or bug fixes.
- Use `git checkout -b <branch-name>` to create and switch to a new branch.
- Merge branches with `git merge`.

---

## **Stashing Changes**
- Use `git stash` to temporarily save changes.
- Restore stashed changes with `git stash pop`.

---

## **Ignoring Files**
- Create a `.gitignore` file to exclude files from being tracked.
- Use patterns to specify files or directories to ignore.

---

## **Pull Requests (PRs)**
1. Create a branch for your changes.
2. Commit and push your changes.
3. Open a PR on GitHub for code review.
4. Merge the PR after approval.

---

## **README Files**
- Use `README.md` to describe your project.
- Include:
  - Project name and description.
  - Installation instructions.
  - Usage examples.
  - Credits and acknowledgments.

---

## **Markdown Syntax**
### **Headers**
- `# H1`
- `## H2`
- `###### H6`

### **Emphasis**
- `*italic*` or `_italic_`
- `**bold**` or `__bold__`

### **Lists**
- Unordered:
  ```markdown
  * Item 1
  * Item 2
    * Subitem 2a
  ```
- Ordered:
  ```markdown
  1. Item 1
  2. Item 2
  ```

### **Images**
- `![alt text](image-url)`

### **Links**
- `[link text](url)`

### **Blockquotes**
- `> This is a blockquote.`

---

## **Final Notes**
- Keep my notes organized and structured.
- Use Git and GitHub to showcase your projects and collaborate effectively.
- Write clear and concise README files to explain your work.
