[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True
android.permissions = INTERNET
p4a.bootstrap = sdl2
p4a.branch = v2023.06.06
p4a.fork = kivy
