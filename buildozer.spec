[app]
title = AT World
package.name = atworld
package.domain = com.atworld.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3==3.11.6,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
p4a.branch = master
p4a.bootstrap = sdl2
