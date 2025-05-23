[app]

# Title of your application
title = Ransomware Simulator

# Package name and domain
package.name = ransomware_simulator
package.domain = org.simulator

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Requirements
requirements = python3,kivy,pycryptodome

# Orientation
orientation = portrait

# Fullscreen mode
fullscreen = 0

# Android permissions
android.permissions = android.permission.INTERNET,android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE

# Android API and architecture
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.ndk_path = /Users/shaileshkumar/Library/Android/sdk/ndk/25.1.8937393

# Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# Enable AndroidX (in case you later use libraries requiring it)
android.enable_androidx = True

# Keep screen on (optional for simulation purposes)
android.wakelock = True

# Allow backup (default is True)
android.allow_backup = True

# Use lib copy method for compatibility
android.copy_libs = 1

# Format for packaging
android.release_artifact = aab
android.debug_artifact = apk

# Logcat filters for debugging
android.logcat_filters = *:S python:D

# Keep the default bootstrap
# p4a.bootstrap = sdl2

# OSX specific settings
osx.python_version = 3
osx.kivy_version = 2.1.0
