# Getting Started with GitHub — IS3020 Python Programming

## One-Time Setup (Do this in Week 1)

### Step 1: Create a GitHub Account
- Go to https://github.com and sign up
- Use your KSU student email (e.g., yourname@students.kennesaw.edu)

### Step 2: Install PyCharm
- Download PyCharm Community (free): https://www.jetbrains.com/pycharm/download/
- Install and open it

### Step 3: Connect PyCharm to GitHub
- Open PyCharm → **Settings → Version Control → GitHub**
- Click **"+"** → **"Log In via GitHub..."**
- Authorize PyCharm in the browser popup
- Your GitHub account should now appear in the list

### Step 4: Fork the Assignment Repo
- Go to: https://github.com/KSU-IS3020Summer/python-assignments
- Click the **"Fork"** button (top right)
- Select your personal account
- You now have your own copy at: `github.com/YOUR-USERNAME/python-assignments`

### Step 5: Clone to PyCharm
- In PyCharm: **Git → Clone...**
- Paste your fork URL: `https://github.com/YOUR-USERNAME/python-assignments.git`
- Choose a folder and click **Clone**
- The project opens with all 10 weeks of assignments

---

## Weekly Workflow

### 1. Open the notebook
- In PyCharm, navigate to the week's folder (e.g., `week01/`)
- Open `exercises.ipynb`
- You should see markdown instructions and code cells

### 2. Write your code
- Click in a code cell
- Write your answer
- Press **Shift+Enter** to run the cell and see output

### 3. Submit your work (3 steps)
1. **Git → Commit** (or Cmd+K on Mac)
2. Type a message like "Complete week 1" in the text box
3. Click **"Commit and Push"**

That's it — your work is now on GitHub.

### 4. Verify on GitHub
- Go to `github.com/YOUR-USERNAME/python-assignments`
- Click on the week folder — you should see your answers

---

## When Professor Updates Assignments

If new assignments or corrections are posted:
1. Go to your fork on GitHub
2. Click **"Sync fork"** → **"Update branch"**
3. In PyCharm terminal: `git pull`

---

## FAQ

### Cloning Issues

**Q: PyCharm says "Clone failed — not found"**
A: This is the most common problem. Try these fixes in order:
1. Make sure you're cloning **YOUR fork** (github.com/YOUR-USERNAME/...), not the class repo
2. Check **Settings → Version Control → GitHub** — your account must be linked
3. If the repo browser doesn't show organization repos, **paste the full URL directly** instead of browsing
4. If it still fails, clone from PyCharm's **terminal** instead:
   ```
   git clone https://github.com/YOUR-USERNAME/python-assignments.git
   ```
   Then open the folder with **File → Open**

**Q: PyCharm's Git menu only shows Commit/Push/Pull but no Clone**
A: You already have a project open. Do **File → Close Project** to go back to the Welcome screen, then click **"Get from VCS"**.

**Q: I see "Get from VCS" but can't find my repo in the list**
A: PyCharm may only show your personal repos, not organization repos. Switch to the **URL** tab and paste your fork URL directly.

### Committing & Pushing Issues

**Q: I edited my code but GitHub doesn't show it**
A: You need to **Commit AND Push**. Just saving is not enough. PyCharm auto-saves files, but that only saves to your computer. You must:
1. **Git → Commit** → type a message → click Commit
2. **Git → Push**
Or use **"Commit and Push"** button to do both at once.

**Q: "Commit operation was cancelled due to empty commit message"**
A: You must type a message in the text box before clicking Commit. The message describes what you changed (e.g., "Complete week 1"). It can be anything — just don't leave it blank.

**Q: PyCharm asks for my email when committing**
A: Enter your KSU email. This labels who made the commit — it's not asking for your password. You only need to do this once.

**Q: I clicked Push but nothing happened on GitHub**
A: You probably pushed without committing first. Push only uploads committed changes. Always Commit first, then Push.

### Understanding Git

**Q: What is Push vs Pull vs Sync?**
A:
- **Push** = upload your work from PyCharm to GitHub
- **Pull** = download updates from GitHub to PyCharm
- **Sync** = does both Pull and Push together

**Q: What is a commit message?**
A: A short note describing what you changed (e.g., "Complete week 3 exercises"). Git requires one every time you save changes. Think of it as a label on your save point.

**Q: What is Fork vs Clone?**
A: **Fork** = create your own copy of a repo on GitHub (done once on the website). **Clone** = download that copy to your computer (done once in PyCharm).

### Notebook Issues

**Q: GitHub website is very slow when I try to edit notebooks**
A: Don't edit notebooks on GitHub's website — it can't handle large .ipynb files. Always edit in PyCharm.

**Q: PyCharm shows raw JSON code instead of the notebook**
A: Right-click the .ipynb file → **Open With → Jupyter Notebook**

**Q: I can't run cells in PyCharm**
A: Make sure Python is configured. Go to **Settings → Project → Python Interpreter** and select a Python installation. Click **Shift+Enter** to run a cell.

### Other

**Q: Can I work on future weeks early?**
A: Yes! All 10 weeks are available. Work at your own pace, but submit before each deadline.

**Q: I accidentally broke my code and want to go back**
A: Git saves every commit. In PyCharm terminal type `git log --oneline` to see your history. Ask Professor Wang for help reverting.

**Q: Professor updated the assignments — how do I get the update?**
A: Go to your fork on GitHub → click **"Sync fork"** → **"Update branch"**. Then in PyCharm terminal: `git pull`
