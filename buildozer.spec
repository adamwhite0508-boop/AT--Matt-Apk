[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworld.matter
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
source.exclude_exts = spec,md
version = 5.0
requirements = python3,kivy==2.3.0,kivymd,pillow,plyer,android,requests
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# === FINAL FIX - Single Arch ===
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.ndk_api = 33
android.accept_sdk_license_agreements = True
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,READ_MEDIA_IMAGES

p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
p4a.setup_py = True

android.release_artifact = aab
android.ant = auto
android.allow_backup = False
android.backup_rules =
android.restore_rules =
android.presplash_color = #FFFFFF
