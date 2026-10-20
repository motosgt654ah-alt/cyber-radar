[app]

# (str) Title of your application
title = Cyber Radar

# (str) Package name
package.name = cyberradar

# (str) Package domain (needed for android packaging)
package.domain = org.mouduapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3, kivy, android, hostpython3, sdl2, pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be 33
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept NDK license automatically
android.accept_sdk_license = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a
