[app]
title = Color Blast
package.name = colorblast
package.domain = com.colorblast

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,pyjnius,plyer

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

android.keystore = 0
android.release_artifact = apk

p4a.bootstrap = sdl2
p4a.requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1
