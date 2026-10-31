[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atmatter.world
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,CAMERA
android.icon = icon.png
android.archs = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
