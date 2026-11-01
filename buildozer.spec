[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
source.include_exts = py,png,jpg,kv,webp
version = 6.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,plyer,pillow,requests
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash_login.png
presplash.background = #ffffff
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a

[buildozer]
log_level = 1
warn_on_root = 1
