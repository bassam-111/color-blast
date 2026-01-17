# Building & Publishing Color Blast APK

## 📋 Prerequisites

Before building for Android, ensure you have:

### Required Software
1. **Python 3.9+** - Already have if main.py runs
2. **Java JDK 11+** - Required for APK compilation
3. **Android SDK** - Required for Android builds
4. **Buildozer** - Python build tool for Kivy

### Installation Commands

```bash
# Install build tools
pip install buildozer cython

# Install Java JDK (Windows)
# Download from: https://www.oracle.com/java/technologies/downloads/

# Install Android SDK
# Download Android Studio from: https://developer.android.com/studio
```

---

## 🛠️ Step-by-Step Build Process

### Step 1: Verify Setup
```bash
# Check Python version
python --version

# Check Java installation
java -version

# Check Kivy
python -c "import kivy; print(kivy.__version__)"
```

### Step 2: Configure buildozer.spec
The file is already configured, but you can customize:

```ini
[app]
title = Color Blast              # App name
package.name = colorblast       # Package name (lowercase)
package.domain = com.colorblast # Domain (reverse)
version = 1.0.0                 # Version number

[app:android]
android.permissions = INTERNET   # Permissions needed
android.api = 31                # Target API
android.minapi = 21             # Minimum API (Android 5.0)
```

### Step 3: Build Debug APK (Testing)
```bash
buildozer android debug
```

**First build takes 10-30 minutes** (downloads Android SDK, compiles code)  
**Subsequent builds are faster (2-5 minutes)**

Output location: `bin/colorblast-1.0.0-debug.apk`

### Step 4: Build Release APK (Play Store)
```bash
buildozer android release
```

Output location: `bin/colorblast-1.0.0-release.apk`

---

## 🔑 Key Build Files & Their Purposes

| File | Purpose |
|------|---------|
| `main.py` | Game source code |
| `buildozer.spec` | Android build configuration |
| `requirements.txt` | Python dependencies |
| `data/icon.png` | App icon (512x512) |
| `data/presplash.png` | Launch splash screen |
| `.buildozer/` | Build cache (auto-created) |
| `bin/` | Output APK files |

---

## 📦 Testing the APK

### Option 1: USB Connected Android Device
```bash
# Enable Developer Mode on your phone:
# Settings > About Phone > tap "Build Number" 7 times
# Settings > Developer Options > enable USB Debugging

# Connect phone via USB and run:
buildozer android debug
buildozer android logcat  # View app logs
```

### Option 2: Android Emulator
1. Open Android Studio
2. Create virtual device (Pixel 4, API 31)
3. Start emulator
4. Run buildozer android debug

### Option 3: Manual Installation
1. Build: `buildozer android debug`
2. Transfer APK to phone via USB/ADB
3. Enable "Unknown Sources" in Settings
4. Tap APK to install

---

## 🐛 Troubleshooting Build Issues

### Problem: "buildozer: command not found"
```bash
pip install --upgrade buildozer
```

### Problem: "Java not found"
```bash
# Set JAVA_HOME environment variable
# Windows: Set in System Properties > Environment Variables
set JAVA_HOME=C:\Program Files\Java\jdk-11.0.x
```

### Problem: "Android SDK not found"
```bash
# Buildozer will download it, or set ANDROID_SDK_ROOT
set ANDROID_SDK_ROOT=C:\Android\sdk
```

### Problem: Build fails with NDK error
```bash
# Clean and rebuild
buildozer android clean
buildozer android debug
```

### Problem: APK too large (>50MB)
- Buildozer caches reduce on 2nd build
- Final APK should be ~5-10MB

---

## 🚀 Uploading to Google Play Store

### Step 1: Create Developer Account
- Visit: https://play.google.com/console
- Pay $25 one-time fee
- Agree to terms and conditions

### Step 2: Create New App
1. Click "Create app"
2. App name: "Color Blast"
3. Category: Games > Puzzle
4. Content rating: Everyone (3+)

### Step 3: Prepare Store Listing
```
Title: Color Blast
Short description: Match colors and blast your way to the top!
Full description: [See PROJECT_SUMMARY.md for template]
Category: Games > Puzzle
Content rating: Everyone
```

### Step 4: Upload APK
1. Click "Releases" > "Create new release"
2. Upload `bin/colorblast-1.0.0-release.apk`
3. Add release notes (e.g., "Initial release")
4. Save

### Step 5: Configure Store Listing
1. Add screenshots (3-5 images)
2. Add feature graphic (1024x500)
3. Set category to "Games > Puzzle"
4. Add privacy policy URL (from your PRIVACY_POLICY.md)
5. Set pricing to "Free"

### Step 6: Submit for Review
1. Review content rating questionnaire
2. Click "Submit for review"
3. Wait 2-24 hours for approval
4. Check email for review result

---

## 📊 Build Configuration Options

### Customize Package Name
```ini
# In buildozer.spec
package.domain = com.yourcompany
package.name = yourapp
```

Result: `com.yourcompany.yourapp`

### Add Permissions
```ini
# Common permissions:
android.permissions = INTERNET
android.permissions = CAMERA
android.permissions = VIBRATE
```

### Change Target API
```ini
# Current (recommended):
android.api = 31

# Newer APIs for Play Store compliance:
android.api = 33  # Android 13
android.api = 34  # Android 14
```

---

## 📱 Testing Checklist

Before submitting to Play Store, test:

- [ ] Game starts without crashes
- [ ] All buttons work (Match, Clear)
- [ ] Selecting/deselecting blocks works
- [ ] Score increases correctly
- [ ] Layout looks good on various screen sizes
- [ ] No permission requests (offline only)
- [ ] App can be installed and uninstalled cleanly
- [ ] No sensitive data in logs

---

## 🔐 Release Build Security

For production release APK:

### Generate Signing Key
```bash
# Create keystore (one-time)
keytool -genkey -v -keystore my-release-key.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias my-key-alias
```

### Configure in buildozer.spec
```ini
android.release_artifact = aab
p4a.release_artifact = aab
```

### Build and Sign
```bash
buildozer android release
# APK will be signed automatically
```

---

## 📈 Optimization Tips

### Reduce APK Size
- Remove unused code from main.py
- Use `buildozer ... -- --release` flag
- Kivy handles most optimization automatically

### Improve Performance
- Reduce number of blocks in game board
- Optimize animation speed
- Use appropriate image compression

### Better Battery Life
- Game runs efficiently
- Minimal background processing
- No constant network checks

---

## 🎯 Version Management

When updating your game:

```ini
# In buildozer.spec
version = 1.0.0  → 1.0.1  (bug fix)
version = 1.0.0  → 1.1.0  (new features)
version = 1.0.0  → 2.0.0  (major overhaul)
```

Then rebuild and upload new APK to Play Store.

---

## 📞 Getting Help

### Resources
- **Kivy**: https://kivy.org/doc/stable/guide/quickstart.html
- **Buildozer**: https://buildozer.readthedocs.io/
- **Android Docs**: https://developer.android.com/docs
- **Google Play**: https://developer.android.com/google-play

### Common Issues
See troubleshooting section in this file or check:
- Buildozer GitHub issues
- Kivy Discord community
- Stack Overflow (tag: kivy)

---

## ✅ Ready to Ship!

Your Color Blast game is production-ready:
- ✓ Code is complete and tested
- ✓ Assets are generated
- ✓ Build configuration is ready
- ✓ Legal documents are included

**Next step:** Build and test the APK, then publish!

---

*Build guide for Color Blast v1.0.0*
