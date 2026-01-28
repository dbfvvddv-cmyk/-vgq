[app]
title = Gaming Vault
package.name = gamingvault
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# (مهم جداً) إعدادات الأندرويد
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# أيقونة التطبيق (يمكنك تغييرها لاحقاً)
# icon.filename = %(source.dir)s/data/icon.png

orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
