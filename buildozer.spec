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
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.release_artifact = aab
p4a.bootstrap = sdl2
p4a.branch = master
android.allow_backup = False
