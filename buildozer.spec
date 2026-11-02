[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_patterns = build,bin,.git,.buildozer,.github,venv,__pycache__
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==2.0.0,Pillow==10.4.0,materialyoucolor,materialshapes
orientation = portrait

[buildozer]
log_level = 1

[app:android]
bootstrap = sdl2
p4a.branch = master
p4a.fork = kivy
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.1
android.accept_sdk_license_agreement = True
android.arch = arm64-v8a
android.archs = arm64-v8a
android.permissions = INTERNET
