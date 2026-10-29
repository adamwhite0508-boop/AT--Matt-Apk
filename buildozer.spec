[app]
title = AT World
package.name = atworld
package.domain = com.atworld.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy==2.3.0,Pillow
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 34.0.0
android.archs = arm64-v8a
p4a.branch = develop
android.accept_sdk_license_agreement = True
