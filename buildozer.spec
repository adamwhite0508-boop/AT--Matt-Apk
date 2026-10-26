[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.at.worldmatter
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.1.1
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 35
android.minapi = 23
android.sdk = 35
android.ndk = 27c
android.accept_sdk_license_agreement = True
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
p4a.source_dir = 
