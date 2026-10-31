[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
version = 2.0
requirements = python3,kivy==2.3.0,kivymd==2.0.0,Pillow
orientation = portrait
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.build_tools_version = 34.0.0
p4a.branch = master
# YE LINE IMPORTANT HAI - Size kam karega
android.archs = arm64-v8a
p4a.bootstrap = sdl2
p4a.local_recipes = 
android.allow_backup = False

[buildozer]
log_level = 1
