[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,plyer,materialyoucolor
orientation = portrait
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/logo.png
[buildozer]
log_level = 2
[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_CONTACTS,WRITE_CONTACTS,CALL_PHONE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES
android.archs = arm64-v8a
