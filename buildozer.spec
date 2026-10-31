[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atmatter.world
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.3
requirements = python3,kivy==2.3.1,kivymd==1.2.0,Pillow,requests
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license_agreements = True
icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/banner.png
presplash.color = #FFFFFF
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2

# --- ADDONS FOR WASM + RAKSHAK + SECURE ---
android.wakelock = True
android.meta-data = 
    com.google.android.gms.version=12451000

[buildozer]
log_level = 2
warn_on_root = 1
