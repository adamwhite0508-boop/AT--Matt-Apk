[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.5
requirements = python3,kivy==2.3.0,kivymd,pillow,plyer,android,requests
# NOTE: google-generativeai ko yaha mat lagao - Ye build ko fail karega! Hamne code me requests se kaam chala liya hai

orientation = portrait

[buildozer]
log_level = 2

[app:android]
# IMPORTANT FIX
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreements = True
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# p4a ka naya version use karo
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2

# AAB ke liye
android.release_artifact = aab
android.ant = auto

[buildozer:android]
# Cache clear
android.allow_backup = False
