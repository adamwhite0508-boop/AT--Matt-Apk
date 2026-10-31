[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
version = 2.0
requirements = python3,kivy==2.3.0,kivymd==2.0.0,Pillow
orientation = portrait
fullscreen = 0

# FINAL - PLAY STORE 100% PASS - Background nahi hai
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, VIBRATE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license_agreement = True
android.features = android.hardware.location.gps, android.hardware.camera
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1
