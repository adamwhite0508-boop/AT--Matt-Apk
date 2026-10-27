[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.at.worldmatter
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.2.0,kivymd
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25.1.8937393
android.arch = arm64-v8a
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
