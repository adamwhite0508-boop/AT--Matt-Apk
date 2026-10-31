[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
version = 5.0
requirements = python3,kivy==2.3.0,kivymd,pillow,plyer,android,requests
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.ndk_api = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
android.release_artifact = aab
android.ant = auto
