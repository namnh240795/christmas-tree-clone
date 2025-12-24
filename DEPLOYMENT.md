# 🚀 Deployment Guide: GitHub Pages

## Quick Setup

### Step 1: Commit your files
```bash
# Add all files (including Image folder)
git add .

# Commit changes
git commit -m "Add Christmas tree project with images"

# Push to GitHub
git push origin main
```

### Step 2: Enable GitHub Pages

#### Via GitHub Website:
1. Open: https://github.com/namnh240795/christmas-tree-clone/settings/pages
2. Select Source: "Deploy from a branch"
3. Select Branch: `main` → `/ (root)`
4. Click Save
5. Wait 1-2 minutes for deployment

#### Via GitHub CLI:
```bash
# Install GitHub CLI if not installed: https://cli.github.com/
gh repo edit --enable-pages --source=branch --branch=main
```

### Step 3: Access your site

Your site will be available at:
```
https://namnh240795.github.io/christmas-tree-clone/
```

## 📸 Important: Images Folder

Make sure your `Image` folder is committed to the repository:

```bash
# Check if Image folder is tracked
git status

# If not tracked, add it
git add Image/
git commit -m "Add Image folder with photos"
git push origin main
```

## 🎯 File Structure on GitHub

Your repository should look like this:
```
christmas-tree-clone/
├── Image/              ← Your photos (must be committed!)
│   ├── 1.png
│   ├── 2.png
│   └── ...
├── index.html          ← Main file
├── server.py           ← (Not needed for GitHub Pages)
├── README.md           ← Documentation
└── .gitignore          ← (optional)
```

## 🔧 Troubleshooting

### Images not loading?
- Make sure `Image/` folder is committed to git
- Check file names match exactly (case-sensitive!)
- Verify images are not in `.gitignore`

### 404 errors?
- Wait a few minutes for GitHub Pages to deploy
- Check GitHub Actions tab for deployment status

### Camera not working?
- GitHub Pages provides HTTPS automatically ✓
- Make sure you're accessing via https:// (not http://)

### Want custom domain?
1. In repository Settings → Pages
2. Click "Use your own domain"
3. Follow the DNS instructions

## 🚀 Bonus: Automatic Deployment

Set up automatic deployment when you push changes:

### GitHub Actions (Optional)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Pages
        uses: actions/configure-pages@v3

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

This creates automatic deployments on every push to main!

## 🎨 Showcase URL

Once deployed, share your Christmas tree:
- Link: `https://namnh240795.github.io/christmas-tree-clone/`
- Share with family and friends! 🎅

## 📝 Notes

- GitHub Pages is free for public repositories
- Server file (`server.py`) is not needed
- All features work the same as local server
- HTTPS is included automatically
