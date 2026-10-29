[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

# FINAL LOGO SETTING
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/banner.png

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
