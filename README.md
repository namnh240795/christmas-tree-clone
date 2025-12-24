# 🎄 Grand Luxury Christmas Tree

A beautiful 3D Christmas tree visualization with AI gestures, touch controls, and photo displays.

## 🚀 Quick Start

### Option 1: Using Python (Recommended)

1. Make sure Python 3 is installed
2. Run the server:
   ```bash
   python3 server.py
   ```
3. Open your browser and go to `http://localhost:8000`

### Option 2: Using Node.js

1. Install a simple HTTP server:
   ```bash
   npx http-server -p 8000
   ```
2. Open `http://localhost:8000` in your browser

### Option 3: Using VS Code Live Server

1. Install the "Live Server" extension
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 📸 Loading Your Images

### Default Images

The tree automatically loads images from the `Image/` folder. Make sure your images are in this folder.

Supported formats: `.jpg`, `.png`, `.jpeg`

### Manual Image Upload

You can also upload images manually:
- Click the **"Select Folder"** button to select a folder of images
- Click the **"Select Files"** button to select individual image files

## 🎮 Controls

### Mouse/Touch
- **Drag** - Rotate the tree
- **Click on photo** - Focus on that photo
- **Double tap** - Switch between Tree and Scatter modes

### Keyboard Shortcuts
- **S** - Toggle stats dashboard
- **H** - Toggle controls visibility

### Gesture Controls (with Camera)
- **Enable Camera** - Click the "📷 Enable Gesture" button
- **Open Hand** - Tree mode
- **Fist** - Scatter mode  
- **Pinch** - Focus on random photo

### Mode Buttons (Bottom)
- 🎄 **Tree Mode** - Photos arranged in spiral on tree
- ✨ **Scatter Mode** - Photos floating in 3D space
- 🔍 **Focus Mode** - Focus on a random photo

## 📦 Project Structure

```
chrismastree/
├── index.html          # Main HTML file
├── server.py           # Python HTTP server
├── Image/             # Your photos folder
│   ├── 1.png
│   ├── 2.png
│   └── ...
└── README.md          # This file
```

## 🎨 Features

- ✨ Beautiful 3D Christmas tree with gold and silver decorations
- 📸 Display your own photos on the tree
- 🎬 Smooth animations and transitions
- 📊 Visitor statistics dashboard
- 🖐️ AI-powered hand gesture controls
- 🎄 Multiple viewing modes
- ❄️ Falling snow effect
- 📱 Fully responsive design

## 🌐 Browser Requirements

- Modern browser with WebGL support
- Chrome, Firefox, Safari, or Edge
- For camera features: HTTPS or localhost

## 📝 Notes

- Images should be placed in the `Image/` folder for automatic loading
- The server must be running in the project root directory
- Camera permissions are required for gesture controls
- Press 'H' to hide UI elements for screenshots

Enjoy your Christmas tree! 🎅✨
