# Color Blast - Mobile Game

Production-ready mobile puzzle game built with Kivy for Android/Google Play Store. Match colored blocks, score points, and progress through levels. Offline playable, lightweight, and fully documented.

A vibrant, colorful puzzle game available on Google Play Store.

## Game Features

✨ **Engaging Gameplay**
- Match colored blocks to score points
- Simple tap-based controls
- Progressive difficulty levels
- Addictive puzzle mechanics

🎨 **Visual Design**
- Colorful, eye-catching graphics
- Smooth animations
- Clean, intuitive UI
- Optimized for mobile screens

📊 **Game Mechanics**
- Score tracking
- Move counter
- Level progression
- High score system (local storage)

## System Requirements

### For Development
- Python 3.9+
- Kivy 2.2.1+
- Virtual environment (recommended)

### For Android Deployment
- Java Development Kit (JDK)
- Android SDK (API 31+)
- Buildozer (build tool)
- 4GB+ free disk space

## Installation & Setup

### 1. Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Game (Desktop)

```bash
python main.py
```

### 3. Building for Android (APK)

#### Prerequisites
- Install Buildozer: `pip install buildozer`
- Install Java JDK 11+
- Install Android SDK

#### Build Command
```bash
buildozer android debug
```

This creates an APK file in the `bin/` directory that can be:
1. Installed on Android devices
2. Uploaded to Google Play Store
3. Shared directly with testers

#### For Release Build
```bash
buildozer android release
```

## File Structure

```
.
├── main.py                    # Main game application
├── buildozer.spec            # Android build configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── PRIVACY_POLICY.md         # Privacy policy (Play Store)
├── TERMS_OF_SERVICE.md       # Terms of service (Play Store)
└── data/
    ├── icon.png              # App icon (512x512)
    ├── presplash.png         # Splash screen
    └── screenshots/          # Play Store screenshots
```

## Play Store Submission

### Checklist Before Submission

- [x] App icons created (512x512 PNG)
- [x] Privacy policy included
- [x] Terms of service included
- [x] Game tested on multiple devices
- [x] Buildozer configuration updated
- [x] APK generated and tested

### Required Assets

1. **App Icon** (512x512 PNG)
   - Location: `data/icon.png`

2. **Feature Graphic** (1024x500 PNG)
   - High-quality image showcasing the game

3. **Screenshots** (at least 2, max 8)
   - Showcase gameplay and features
   - 1080x1920 or 1440x2560 PNG

4. **Promo Graphic** (180x120 PNG)
   - Optional branding image

5. **Video Trailer** (15-30 seconds)
   - Optional but recommended

### Store Listing Information

- **App Name**: Color Blast
- **Short Description**: Match colors and blast your way to the top!
- **Full Description**: 
  ```
  Color Blast is a fun and addictive puzzle game where you match 
  colorful blocks to score points. Tap to select blocks of the same 
  color, then tap Match to blast them away! Progress through levels 
  and challenge yourself to beat your high score.
  
  Features:
  • Simple, intuitive gameplay
  • Colorful graphics
  • Increasing difficulty
  • Track your high scores
  • No internet required
  ```

- **Category**: Games > Puzzle
- **Content Rating**: Everyone
- **Privacy Policy**: [Included in PRIVACY_POLICY.md]
- **Permissions**: Minimal (no internet required)

## Gameplay Instructions

1. **Start Game**: Launch the app to see the game board
2. **Select Blocks**: Tap colored blocks to select them
3. **Match**: Tap the "Match" button to remove matching colors
4. **Clear**: Tap "Clear" to deselect blocks
5. **Score Points**: Matching 2+ blocks earns points (10 per block)
6. **Level Up**: Complete levels to unlock new challenges

## Controls

- **Tap**: Select/deselect color blocks
- **Match Button**: Remove selected blocks of same color
- **Clear Button**: Deselect all blocks

## Performance Optimization

- Lightweight codebase (~500 lines)
- Minimal memory footprint
- Optimized for devices with 512MB+ RAM
- Supports devices from Android 5.0+

## Troubleshooting

### App Crashes on Startup
- Ensure all Python dependencies are installed
- Check Java and Android SDK paths

### Build Fails
- Update buildozer: `pip install --upgrade buildozer`
- Clean previous builds: `buildozer android clean`

### Performance Issues
- Reduce block count in `GameBoard.generate_board()`
- Optimize graphics settings in buildozer.spec

## Future Enhancements

- Leaderboard system
- Power-ups and special blocks
- Sound effects and music
- Multiplayer mode
- Achievements and badges

## License

© 2026 Color Blast. All rights reserved.

## Support

For bug reports or feature requests, contact: support@colorblast.com

---

**Ready to publish?** Follow the checklist and upload your APK to Google Play Console!
