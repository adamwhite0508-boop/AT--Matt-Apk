[app]
title = AT Matt Apk
package.name = org.atmattapk
package.domain = org.atmattapk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
p4a.ndk_api = 21
android.build_tools_version = 33.0.2
p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = master
