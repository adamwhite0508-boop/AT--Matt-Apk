[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.anuj.atworldmatter
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.6
requirements = python3,kivy==2.3.0,kivymd==1.1.1
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 28c
android.sdk = 33
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
