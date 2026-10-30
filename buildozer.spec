[app]
title = AT World Mater
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.1
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,plyer,materialyoucolor
orientation = portrait
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/banner.png
presplash.enforce = True

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_CONTACTS,CALL_PHONE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
