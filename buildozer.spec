[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.at.worldmatter
source.dir = .
source.include_exts = py,png,kv
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/icon.png
orientation = portrait
[app:android]
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_CONTACTS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.build_tools_version = 33.0.2
