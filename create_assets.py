#!/usr/bin/env python3
"""
Generate placeholder assets for Color Blast
Run this script to create icon.png and presplash.png
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create icon.png (512x512)
    icon = Image.new('RGBA', (512, 512), (240, 240, 245, 255))
    draw = ImageDraw.Draw(icon)
    
    # Draw colorful blocks pattern
    colors = [
        (255, 51, 51),      # Red
        (51, 179, 255),     # Blue
        (51, 255, 102),     # Green
        (255, 255, 51),     # Yellow
        (255, 153, 51),     # Orange
        (255, 51, 255),     # Purple
    ]
    
    block_size = 85
    spacing = 5
    offset = 10
    
    for i, color in enumerate(colors):
        row = i // 3
        col = i % 3
        x = offset + col * (block_size + spacing)
        y = offset + row * (block_size + spacing)
        draw.rectangle(
            [x, y, x + block_size, y + block_size],
            fill=color,
            outline=(100, 100, 100),
            width=2
        )
    
    # Add text
    try:
        # Try to use default font, fallback to default if not available
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    text = "Color Blast"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (512 - text_width) // 2
    text_y = 380
    
    draw.text((text_x, text_y), text, fill=(50, 50, 50), font=font)
    
    icon.save('data/icon.png')
    print("✓ Created data/icon.png (512x512)")
    
    # Create presplash.png (720x1280)
    presplash = Image.new('RGB', (720, 1280), (240, 240, 245))
    draw = ImageDraw.Draw(presplash)
    
    # Draw gradient effect with color blocks
    for i in range(6):
        for j in range(3):
            x = 60 + j * 220
            y = 200 + i * 120
            draw.rectangle(
                [x, y, x + 180, y + 100],
                fill=colors[i % 6],
                outline=(100, 100, 100),
                width=2
            )
    
    # Add title
    try:
        title_font = ImageFont.truetype("arial.ttf", 70)
        subtitle_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    title = "Color Blast"
    subtitle = "Match. Blast. Score!"
    
    # Center title
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(
        ((720 - title_width) // 2, 950),
        title,
        fill=(50, 50, 50),
        font=title_font
    )
    
    # Center subtitle
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(
        ((720 - subtitle_width) // 2, 1050),
        subtitle,
        fill=(100, 100, 100),
        font=subtitle_font
    )
    
    presplash.save('data/presplash.png')
    print("✓ Created data/presplash.png (720x1280)")
    
    print("\nAssets created successfully!")
    print("You can now build the APK with: buildozer android debug")
    
except ImportError:
    print("PIL (Pillow) not installed. Installing...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'pillow'])
    print("Please run this script again.")
except Exception as e:
    print(f"Error creating assets: {e}")
    print("Manual assets will need to be created.")
