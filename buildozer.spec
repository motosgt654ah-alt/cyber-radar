[app]

# (str) Title of your application
title = MeuApp

# (str) Package name
package.name = meuapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.meuapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Usando kivy==2.2.1 estavel para evitar erros de versao no pip
requirements = python3, kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# android.permissions = INTERNET

#
# Android specific
#

# (bool) Indicate if the application should be foreground only
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = warning)
warn_on_root = 1
