[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
version = 2.0
requirements = python3,kivy==2.3.0,kivymd==2.0.0,Pillow
orientation = portrait
android.permissions = INTERNET, CAMERA

# YE 5 LINE PAKKA ADD KARO - LICENSE FIX
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.build_tools_version = 34.0.0
android.ant_path = /usr/bin/ant
p4a.branch = master

[buildozer]
log_level = 2
