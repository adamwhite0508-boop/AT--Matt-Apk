[app]
title = AT World Mater
package.name = atworldmater
package.domain = com.atworld.mater
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,requests,androidstorage4kivy
orientation = portrait
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True

[buildozer]
log_level = 2
warn_on_root = 1
