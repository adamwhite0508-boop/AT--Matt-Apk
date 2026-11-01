[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.0,kivymd==1.1.1,pillow,plyer,android
orientation = portrait

[buildozer]
log_level = 2

# Android wale
p4a.branch = master
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA,RECORD_AUDIO,ACCESS_FINE_LOCATION
