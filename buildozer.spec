[app]
title = AT World Mater
package.name = atworldmater
package.domain = com.atworld.mater
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db
version = 1.0
requirements = python3,kivy,requests,androidstorage4kivy
orientation = portrait
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_CONTACTS,RECORD_AUDIO
android.api = 33
[buildozer]
log_level = 2
warn_on_root = 1
