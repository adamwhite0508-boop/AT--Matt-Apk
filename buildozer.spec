[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.permissions = INTERNET,RECORD_AUDIO
android.icon = icon.png
android.build_tools_version = 34.0.0
android.archs = arm64-v8a
p4a.branch = develop
