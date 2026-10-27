[app]
title = AT Matt Apk
package.name = org.atmattapk
package.domain = org.atmattapk
source.dir = .
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
android.build_tools_version = 33.0.2
android.archs = arm64-v8a
