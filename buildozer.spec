[app]

title = BTC 5分钟预测
package.name = btc5min
package.domain = org.btc5min
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,requests,pandas,numpy,scikit-learn
orientation = portrait
author = © BTC 5分钟预测

# Android specific
fullscreen = 0
android.permissions = android.permission.INTERNET, android.permission.ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.enable_androidx = True
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.release_artifact = apk
android.debug_artifact = apk

# Python for android (p4a) specific
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
