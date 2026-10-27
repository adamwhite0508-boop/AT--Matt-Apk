[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
p4a.branch = master
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
