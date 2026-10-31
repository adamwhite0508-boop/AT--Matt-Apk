[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atmatter.world
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.2
requirements = python3,kivy==2.2.0,kivymd==1.2.0,Pillow
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license_agreements = True
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/banner.png
presplash.color = #FFFFFF
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
