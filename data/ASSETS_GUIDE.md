# Asset Creation Guide

This file explains how to create the required assets for Color Blast.

## Required Assets

### 1. App Icon (icon.png)
- **Size**: 512x512 pixels
- **Format**: PNG with transparency
- **Description**: A colorful, vibrant icon that represents the app
- **Tools**: Photoshop, GIMP, Canva, or any image editor

### 2. Presplash Image (presplash.png)
- **Size**: 720x1280 pixels
- **Format**: PNG
- **Description**: Splash screen shown on app launch
- **Content**: App logo/name with game aesthetic

### 3. Play Store Screenshots
- **Size**: 1080x1920 or 1440x2560 pixels
- **Format**: PNG
- **Quantity**: 2-8 images
- **Content**: Showcase main gameplay, features, and interface

## How to Create Assets (No Design Skills Needed)

### Quick Option 1: Use Canva (Free)
1. Go to canva.com
2. Create new design → Select dimension (512x512, 720x1280, etc.)
3. Choose "Puzzle Game" templates
4. Customize with colors and text
5. Download as PNG
6. Save to `data/` folder

### Quick Option 2: Use GIMP (Free, Open Source)
1. Download GIMP from gimp.org
2. Create new image with required dimensions
3. Design using built-in tools
4. Export as PNG
5. Save to `data/` folder

### Quick Option 3: Use Online Tools
- Pixlr (pixlr.com) - Browser-based image editor
- Photopea (photopea.com) - Web version of Photoshop
- Both support PNG export

## Color Palette for Consistency

Use these colors to match the game theme:
- Red: #FF3333
- Blue: #33B3FF
- Green: #33FF66
- Yellow: #FFFF33
- Orange: #FF9933
- Purple: #FF33FF

## Minimum Setup for Play Store

1. App Icon (512x512)
2. Presplash (720x1280)
3. At least 2 screenshots (1080x1920)

## File Naming Convention

```
data/
├── icon.png          ← App icon (512x512)
├── presplash.png     ← Splash screen (720x1280)
└── screenshots/
    ├── screen1.png   ← Gameplay screenshot
    ├── screen2.png   ← Feature showcase
    └── screen3.png   ← User review / high score
```

## Screenshots Content Ideas

1. **Gameplay Screenshot**
   - Show the game board with colored blocks
   - Display score and moves remaining
   - Include action shots of blocks being matched

2. **Feature Showcase**
   - Show level progression
   - Display high score tracking
   - Highlight colorful design

3. **User Experience**
   - Show controls and buttons
   - Display touch interactions
   - Showcase game over screen

## Important Notes

- All images must be in PNG format
- Use a transparent background where appropriate (except presplash)
- Ensure text is readable on mobile screens
- Test screenshots on actual mobile display
- Keep file sizes reasonable (compress if needed)

## Next Steps

1. Create your assets using one of the suggested tools
2. Save them to the `data/` folder
3. Run `buildozer android debug` to create APK
4. Test on Android device
5. Upload assets to Google Play Console

## Support

- Canva tutorials: youtube.com (search "Canva")
- GIMP tutorials: gimp.org/tutorials
- Game icon resources: game-icons.net, flaticon.com
