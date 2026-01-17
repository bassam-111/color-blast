# Color Blast 🎨💥

**Production-ready mobile puzzle game built with Kivy for Android/Google Play Store.**

Match colored blocks, score points, and progress through levels. Fully offline playable, lightweight, and ready for deployment!

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Android-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎮 Game Features

- **5x6 Grid Puzzle**: Engaging grid-based gameplay with strategic block matching
- **6 Vibrant Colors**: Red, Green, Blue, Yellow, Magenta, and Cyan blocks
- **Tap to Match**: Simple tap-to-select matching mechanics
- **Smart Scoring**: Earn 10 points per block removed
- **Move Counter**: Track your efficiency with move counting
- **Level Progression**: Progress through increasingly challenging levels
- **Target Score System**: Reach target scores to advance (500, 1000, 1500, etc.)
- **100% Offline**: No internet connection required - play anywhere, anytime
- **Lightweight**: Minimal storage and resource usage
- **Clean UI**: Intuitive interface suitable for all ages

## 🎯 Gameplay

1. **Tap a colored block** to select all connected blocks of the same color
2. **Tap again** to remove the selected blocks and score points
3. **Blocks fall** using gravity physics to fill empty spaces
4. **New blocks appear** at the top to maintain the grid
5. **Reach the target score** to level up and face new challenges
6. **Track your moves** to improve your strategy

### Scoring System
- Each removed block = **10 points**
- Larger groups = Higher scores (e.g., 5 blocks = 50 points)
- Strategic matching is key to reaching target scores efficiently

### Level Progression
- **Level 1**: Target score of 500 points
- **Level 2**: Target score of 1000 points
- **Level 3**: Target score of 1500 points
- Levels continue to increase by 500 points each

## 🚀 Installation

### For Players

1. Download the APK from the releases section
2. Enable "Install from Unknown Sources" in Android settings
3. Install the APK
4. Launch and play!

### For Developers

#### Prerequisites
- Python 3.7+
- Kivy 2.1.0+
- Buildozer (for Android builds)

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/bassam-111/color-blast.git
cd color-blast

# Install Python dependencies
pip install -r requirements.txt

# Run the game locally (for development)
python main.py
```

#### Building for Android

```bash
# Install Buildozer
pip install buildozer

# Install Android SDK dependencies (first time only)
buildozer android debug

# Build APK
buildozer android debug

# Build release APK (for Play Store)
buildozer android release
```

The APK will be generated in `bin/` directory.

## 📁 Project Structure

```
color-blast/
├── main.py                 # Main game logic and Kivy app
├── buildozer.spec          # Android build configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── PRIVACY_POLICY.md      # Privacy policy for Play Store
├── TERMS_OF_SERVICE.md    # Terms of service
└── .gitignore            # Git ignore rules
```

## 🔧 Technical Details

### Architecture
- **Framework**: Kivy 2.1.0 (Python-based mobile framework)
- **Platform**: Android (API 21+, Android 5.0+)
- **Language**: Python 3
- **Architecture Support**: ARM64-v8a, ARMv7

### Game Components

#### `ColorBlock` Class
Represents individual colored blocks in the grid with:
- Color management (6 predefined colors)
- Selection state tracking
- Visual feedback for selection

#### `GameBoard` Class
Manages the 5x6 game grid with:
- Block creation and positioning
- Connected block detection (flood fill algorithm)
- Gravity physics for falling blocks
- New block generation

#### `ColorBlastGame` Class
Main game controller featuring:
- Score tracking and display
- Move counter
- Level progression system
- UI layout and management
- Game reset functionality

## 📱 Google Play Store Submission

### Included Assets
- ✅ Complete source code
- ✅ Buildozer.spec for APK generation
- ✅ Privacy Policy (PRIVACY_POLICY.md)
- ✅ Terms of Service (TERMS_OF_SERVICE.md)
- ✅ README with comprehensive documentation

### Pre-Submission Checklist
- [x] Game is fully functional offline
- [x] No data collection or tracking
- [x] Privacy policy included
- [x] Terms of service included
- [x] Appropriate age rating (suitable for all ages)
- [x] No ads or in-app purchases
- [x] No internet permissions required
- [ ] Create app icon (512x512 PNG for Play Store)
- [ ] Create feature graphic (1024x500 PNG)
- [ ] Take screenshots for store listing
- [ ] Sign APK with release keystore

### Play Store Requirements Met
✅ **Privacy Policy**: See PRIVACY_POLICY.md  
✅ **Terms of Service**: See TERMS_OF_SERVICE.md  
✅ **No Personal Data Collection**: Fully offline game  
✅ **Content Rating**: Suitable for all ages (E for Everyone)  
✅ **Minimum SDK**: API 21 (Android 5.0)  
✅ **Target SDK**: API 31 (Android 12)  

## 🎨 Customization

### Changing Colors
Edit the `COLORS` list in `ColorBlock` class (main.py):
```python
COLORS = [
    (1, 0, 0, 1),      # Red
    (0, 1, 0, 1),      # Green
    (0, 0, 1, 1),      # Blue
    (1, 1, 0, 1),      # Yellow
    (1, 0, 1, 1),      # Magenta
    (0, 1, 1, 1),      # Cyan
]
```

### Adjusting Difficulty
Modify these variables in `ColorBlastGame.__init__`:
```python
self.target_score = 500        # Initial target score
# In level_up method:
self.target_score = self.level * 500  # Score increment per level
```

### Changing Grid Size
Modify in `GameBoard` class:
```python
ROWS = 6  # Number of rows
COLS = 5  # Number of columns
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Game won't start on Android  
**Solution**: Ensure your device runs Android 5.0+ (API 21+)

**Issue**: Buildozer fails to build  
**Solution**: Install build dependencies: `sudo apt-get install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`

**Issue**: Blocks don't fall after removal  
**Solution**: This is handled automatically by the `apply_gravity()` method. If issues persist, check that animations are not disabled.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Guidelines
1. Maintain offline-only functionality
2. Keep code clean and commented
3. Test thoroughly on Android devices
4. Follow Python PEP 8 style guidelines
5. Update documentation for any new features

## 👨‍💻 Author

**Bassam**
- GitHub: [@bassam-111](https://github.com/bassam-111)

## 🙏 Acknowledgments

- Built with [Kivy](https://kivy.org/) - Open source Python framework
- Inspired by classic match-3 puzzle games
- Thanks to the open-source community

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: support@colorblast.com

## 🎯 Roadmap

Future enhancements being considered:
- [ ] Sound effects and background music
- [ ] Power-ups and special blocks
- [ ] Timed challenge mode
- [ ] Daily challenges
- [ ] Achievement system
- [ ] Themes and customization options

## 📊 Version History

### Version 1.0.0 (Current)
- Initial release
- Core gameplay mechanics
- 5x6 grid with 6 colors
- Score tracking and level progression
- Offline functionality
- Play Store ready

---

**Ready for Google Play Store submission! 🚀**

*A simple, fun, and addictive puzzle game that's completely free and respects your privacy.*
