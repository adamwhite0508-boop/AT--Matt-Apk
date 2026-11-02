# Sahi buildozer.spec banao - ye wala 100% working hai KivyMD 2.0.0 ke liye
%%writefile buildozer.spec
[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==2.0.0,Pillow==10.4.0,materialyoucolor==1.0.0,materialshapes
orientation = portrait

[buildozer]
log_level = 2

[app:android]
bootstrap = sdl2
p4a.branch = master
p4a.fork = kivy
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
android.permissions = INTERNET
