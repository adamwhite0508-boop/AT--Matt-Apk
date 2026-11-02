[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = icon.png,login_banner.png
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,Pillow==10.4.0
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2

[app:android]
bootstrap = sdl2
p4a.branch = master
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
