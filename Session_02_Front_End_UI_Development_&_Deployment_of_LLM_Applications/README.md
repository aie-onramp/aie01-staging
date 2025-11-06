<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Front End UI Development & Deployment of LLM Applications</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE8/tree/main/00_AIM_Quicklinks)

| ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|
| Lesson 2 Recording Coming Soon | Lesson 2 Slides Coming Soon | You are here! | Lesson 2 Feedback Form Coming Soon!

Welcome! This guide will walk you through two demos that showcase modern development workflows using v0, Cursor, and best practices.

---

## Prerequisites

Before we begin, make sure you have:
- [Cursor](https://cursor.sh/) installed
- A GitHub account
- A Vercel account (free tier works great!)
- Node.js installed on your computer (use Mac: 'brew install node', Windows: 'sudo apt install nodejs npm')

---

# 🎬 DEMO 1: Setting Up Rules & Creating Your First App

## Overview

In this demo, we'll:
1. **Showcase Cursor rules** by adding GitFlow rules and personal cursor rules (coding styles) to improve collaboration
2. **Showcase v0** - create a vibecode frontend using personal practices
3. **Download and showcase locally** - run the app on your machine
4. **Push to GitHub and deploy** - get your app live on the web

---

## Step 1: Set Up Cursor Rules 📝

### 1.1 Add GitFlow Rules

Set up GitFlow rules to maintain clean version control:

1. Open your project in Cursor
2. Navigate to `gitflow_rules.md` (or create it if it doesn't exist)
3. Add your project-specific GitFlow rules
4. This helps maintain clean version control throughout development

**Example GitFlow rules:**
- Branch naming conventions
- Commit message formats
- Merge strategies
- Release workflow

### 1.2 Add Personal Cursor Rules (Coding Styles)

Set up coding style rules to improve collaboration:

1. Create or update `cursor_rules.md` in your project
2. Add coding standards such as:
   - Code structure & organization
   - Naming conventions (camelCase, PascalCase, UPPER_SNAKE_CASE)
   - Import paths
   - File size limits
   - Component organization

**Why this matters:** These rules help Cursor understand your coding preferences and maintain consistency across your project, making collaboration smoother.

---

## Step 2: Brainstorm Your Idea 💡

First, you need an idea for your app! You have two options:

**Option A: Use v0 for brainstorming**
- Go to [v0.dev](https://v0.dev)
- Use the chat to explore ideas and get suggestions

**Option B: Use ChatGPT (Recommended)**
- Ask ChatGPT to help you brainstorm app ideas
- Get feedback on your concept
- Refine your idea until you're happy with it

---

## Step 3: Get Your Design Resources 🎨

Now it's time to gather design inspiration and components. You have two paths:

#### Path A: Use v0's Premade Templates
- Browse v0's template library
- Pick a template that matches your vision

#### Path B: Create Your Own Design (More Original!)

**a) Pick a Template Style:**
- Visit [Canva Templates](https://www.canva.com/templates/)
- Find a design style you like
- Note the colors, layout, and overall aesthetic

**b) Choose Component Styles:**
- Go to [shadcn/ui Components](https://ui.shadcn.com/docs/components/)
- Browse the component library
- Pick components that match your app's needs (buttons, cards, forms, etc.)

**c) Select a Color Scheme:**
- Visit [Coolors](https://coolors.co/)
- Generate or browse color palettes
- Pick colors that match your app's mood and purpose

---

## Step 4: Create Your v0 Prompt 🎬

Now combine everything into a detailed prompt for v0:

1. Describe your app idea
2. Reference the template style you chose
3. Mention the shadcn/ui components you want to use
4. Include your color scheme
5. Add any specific features or requirements

**Example prompt structure:**
```
Create me an app: [Your App Name]

[Description of your app concept]

Use the design style similar to: [Canva template reference]
For components, use shadcn/ui with: [component names]
Color scheme: [your colors from Coolors]
```

---

## Add GitFlow Rules 📝

Before downloading your app, set up GitFlow rules:

1. Open your project in Cursor
2. Navigate to `gitflow_rules.md` (or create it if it doesn't exist)
3. Add your project-specific GitFlow rules
4. This helps maintain clean version control throughout development

---

## Step 5: Create Virtual Environment 🏗️

Set up your development environment:

1. Open Cursor's terminal
2. Create a virtual environment (if using Python) or ensure Node.js is ready
3. Navigate to your project directory

---

## Step 6: Download Your App from v0 📥

1. In v0, after generating your app, click **"Download"**
2. Copy the download command or use the provided link
3. In Cursor's terminal, run the download command
4. This will create your app folder with all the code

---

## Step 7: Generate README with Cursor 🤖

Let Cursor help you create documentation:

1. In Cursor, ask: *"Create a README.md file explaining how to launch this app"*
2. Cursor will analyze your project structure
3. It will generate a README with setup and launch instructions
4. Review and customize as needed

---

## Step 8: Set Up and Run Locally 🏃

### 8.1 Navigate to App Directory
```bash
cd app
```

### 8.2 Install Dependencies
```bash
npm install
```

This installs all the packages your app needs to run.

### 8.3 Run Your App Locally
```bash
npm run dev
```

Your app should now be running! Look for a local URL (usually `http://localhost:3000`) in the terminal.

**Showcase your app locally!** Open the URL in your browser and see your creation come to life.

---

## Step 9: Push to GitHub 🐙

1. Create a new repository on GitHub
2. In Cursor terminal, initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```
4. Push your code:
   ```bash
   git push -u origin main
   ```

---

## Step 10: Deploy to Vercel 🌐

1. Go to [Vercel](https://vercel.com)
2. Sign in with your GitHub account
3. Click **"New Project"**
4. Import your GitHub repository
5. Vercel will automatically detect your framework
6. Click **"Deploy"**
7. Wait a few minutes, and your app will be live! 🎉

**Your app is now deployed and accessible to the world!**

---
## 🎯 Breakout Room Activity

Now it's your turn to experiment and get creative! Use this time to practice what you've learned and explore the tools.

### Basic Activity

**Experiment with Design Customization:**
- Test out different background styles and color schemes
- Try different button styles and components from shadcn/ui
- Make design changes using v0 to see how it generates updated code
- Practice iterating on your app's visual design

### Advanced Challenge (Optional)

**Build a Fully Functional Frontend App:**
- Try to create a functioning app with interactive features
- Challenge yourself to build features that work entirely in the frontend
- See how far you can get without needing any backend Python scripts
- Explore what's possible with client-side JavaScript, React state management, and browser APIs

**Tip:** Think about apps that can work with local storage, browser APIs, or client-side data processing. Examples: calculators, todo lists, form builders, interactive dashboards, or data visualization tools.
---
# 🎬 DEMO 2: Multi-Agent Workflow & Branch Development

## Overview

In this demo, we'll:
1. **Use the downloaded frontend in Cursor**
2. **Show multi-agent flow** - demonstrate how we can multitask and make different changes simultaneously
3. **Use branch development and best practices** - work with feature branches
4. **Show on GitHub branches** - visualize the branching structure
5. **Demonstrate merging** - merge branches using best practices
6. **Show the final result in Vercel** - see how changes propagate to production

---

## Step 1: Set Up Your Development Environment 🏗️

1. Open the downloaded frontend project in Cursor
2. Ensure you have the latest code from GitHub:
   ```bash
   git pull origin main
   ```
3. Verify your app still runs locally:
   ```bash
   npm run dev
   ```

---

## Step 2: Create Feature Branches 🌿

We'll create multiple branches to work on different features simultaneously, demonstrating multi-agent workflow.

### 2.1 Create Branch for Feature 1

```bash
git checkout -b feature/add-new-component
git push -u origin feature/add-new-component
```

### 2.2 Create Branch for Feature 2

```bash
git checkout -b feature/improve-styling
git push -u origin feature/improve-styling
```

### 2.3 Create Branch for Feature 3

```bash
git checkout -b feature/add-animations
git push -u origin feature/add-animations
```

**Tip:** Each branch represents work that can be done in parallel, simulating a multi-agent workflow where different tasks are handled simultaneously.

---

## Step 3: Multi-Agent Workflow in Cursor 🤖

### 3.1 Work on Feature 1

1. Switch to `feature/add-new-component`:
   ```bash
   git checkout feature/add-new-component
   ```

2. In Cursor, use AI to add a new component:
   - Ask Cursor: *"Add a new [component name] component with [specific features]"*
   - Cursor will generate the code following your cursor rules
   - Review and commit:
     ```bash
     git add .
     git commit -m "feat: add new component"
     git push origin feature/add-new-component
     ```

### 3.2 Work on Feature 2 (Parallel)

1. Switch to `feature/improve-styling`:
   ```bash
   git checkout feature/improve-styling
   ```

2. In Cursor, improve styling:
   - Ask Cursor: *"Update the styling for [component/page] to match [design requirements]"*
   - Cursor will apply changes following your coding standards
   - Review and commit:
     ```bash
     git add .
     git commit -m "style: improve component styling"
     git push origin feature/improve-styling
     ```

### 3.3 Work on Feature 3 (Parallel)

1. Switch to `feature/add-animations`:
   ```bash
   git checkout feature/add-animations
   ```

2. In Cursor, add animations:
   - Ask Cursor: *"Add smooth animations to [components] using [animation library]"*
   - Cursor will implement animations
   - Review and commit:
     ```bash
     git add .
     git commit -m "feat: add animations"
     git push origin feature/add-animations
     ```

**This demonstrates multi-agent workflow:** Different features are being developed simultaneously on separate branches, just like multiple developers working in parallel!

---

## Step 4: View Branches on GitHub 🌐

1. Go to your GitHub repository
2. Click on the **"branches"** dropdown
3. You'll see all your feature branches:
   - `main`
   - `feature/add-new-component`
   - `feature/improve-styling`
   - `feature/add-animations`

4. Click on each branch to see:
   - The commits made on that branch
   - The files changed
   - The diff view showing what was modified

**This visualizes the branching structure and shows how work is organized.**

---

## Step 5: Merge Branches Using Best Practices 🔀

### 5.1 Merge Feature 1

1. Switch to main and pull latest:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Merge feature branch:
   ```bash
   git merge --no-ff feature/add-new-component -m "Merge feature: add new component"
   ```

3. Push to main:
   ```bash
   git push origin main
   ```

### 5.2 Merge Feature 2

1. Ensure main is up to date:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Merge feature branch:
   ```bash
   git merge --no-ff feature/improve-styling -m "Merge feature: improve styling"
   ```

3. Push to main:
   ```bash
   git push origin main
   ```

### 5.3 Merge Feature 3

1. Ensure main is up to date:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Merge feature branch:
   ```bash
   git merge --no-ff feature/add-animations -m "Merge feature: add animations"
   ```

3. Push to main:
   ```bash
   git push origin main
   ```

**Best Practices Demonstrated:**
- Using `--no-ff` to preserve branch history
- Meaningful commit messages
- Merging one feature at a time
- Pulling latest changes before merging

---

## Step 6: Clean Up Branches 🧹

After merging, clean up local and remote branches:

```bash
# Delete local branches
git branch -d feature/add-new-component
git branch -d feature/improve-styling
git branch -d feature/add-animations

# Delete remote branches
git push origin --delete feature/add-new-component
git push origin --delete feature/improve-styling
git push origin --delete feature/add-animations
```

---

## Step 7: View Result in Vercel 🌐

1. Go to your Vercel dashboard
2. Vercel automatically detects the new commits on `main`
3. A new deployment will be triggered automatically
4. Wait for the deployment to complete
5. Visit your live site - you'll see all the merged features!

**This demonstrates:**
- How changes flow from development → GitHub → Vercel
- Automatic deployments on merge to main
- The complete CI/CD workflow

---

## 💅 Example: "Hot Mess Tracker" App

> 🌐 **Live Demo:** You can view the deployed app here: [https://v0-hot-mess-tracker-app.vercel.app/](https://v0-hot-mess-tracker-app.vercel.app/)

Here's the complete prompt we'll use in class for our example app:

### App Prompt for v0:

```
Create me an app: "Hot Mess Tracker"

A "self-report" app for chaos level of your day.

Concept:
- Sliders: "Late to class," "Lost charger," "Sent risky text," "Procrastination"
- Animated emoji face reacts as your "hot mess score" increases
- Saves your results and gives sarcastic motivational message like: "At least you're consistently chaotic. We love that for you"

Design Requirements:
- Use the website style similar to: https://www.canva.com/templates/EAFSoi3Ltnc/
- Similar style background
- For buttons, use this style:

import { ArrowUpIcon } from "lucide-react"
import { Button } from "@/components/ui/button"

export function ButtonDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2 md:flex-row">
      <Button variant="outline">Button</Button>
      <Button variant="outline" size="icon" aria-label="Submit">
        <ArrowUpIcon />
      </Button>
    </div>
  )
}

Color Scheme (for Tailwind CSS):
- murrey: #89023e (hsla(333, 97%, 27%, 1))
- old-rose: #cc7178 (hsla(355, 47%, 62%, 1))
- misty-rose: #ffd9da (hsla(358, 100%, 93%, 1))
- misty-rose-2: #f3e1dd (hsla(11, 48%, 91%, 1))
- tea-green: #c7d9b7 (hsla(92, 31%, 78%, 1))
```

### Tailwind Color Configuration

Add these colors to your `tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'murrey': '#89023e',
        'old-rose': '#cc7178',
        'misty-rose': '#ffd9da',
        'misty-rose-2': '#f3e1dd',
        'tea-green': '#c7d9b7',
      }
    }
  }
}
```

---

## 🎓 Tips for Success

- **Take your time** with each step - don't rush!
- **Experiment** with different designs and components
- **Ask questions** if you get stuck
- **Save your work** frequently (git commits!)
- **Use branches** for every feature - it's a best practice!
- **Review code** before merging
- **Have fun** - this is your chance to be creative!

---