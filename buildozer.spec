[app]
title = AT World Mater
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 5.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,plyer
orientation = portrait
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/banner.png

[buildozer]
log_level = 2

[app:android]
android.api = 34
android.minapi = 23
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_CONTACTS,CALL_PHONE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE,POST_NOTIFICATIONS
android.release_artifact = aab
p4a.bootstrap = sdl2
