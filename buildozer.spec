[app]
title = AT World Mater
package.name = atworldmater
package.domain = com.atworld.mater
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
version.regex = __version__ = ['"](.*)['"]
requirements = python3,kivy==2.3.1
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.arch = armeabi-v7a
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
p4a.whitelist = 

[buildozer]
log_level = 1
warn_on_root = 0
