[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,Pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
bootstrap = sdl2
p4a.branch = develop
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
android.permissions = INTERNET
