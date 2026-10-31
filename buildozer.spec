[app]
title = AT World Matter
package.name = atworldmatter
package.domain = com.atmatter.world
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,Pillow,kivymd
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
p4a.fork = kivy
p4a.branch = stable
p4a.bootstrap = sdl2
