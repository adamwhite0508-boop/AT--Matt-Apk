[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atworldmatter.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = assets/*,images/*,*.png,*.jpg
source.exclude_exts = spec,md,yml,yaml

version = 1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy==2.3.0,kivymd==1.2.0,Pillow
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
bootstrap = sdl2
p4a.branch = develop
p4a.bootstrap = sdl2

android.api = 33
android.minapi = 24
android.ndk = 28c
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True

android.archs = arm64-v8a
android.allow_backup = False

android.permissions = INTERNET

# icon (agar hai to)
# android.icon = icon.png
# presplash color
android.presplash_color = #FFFFFF
