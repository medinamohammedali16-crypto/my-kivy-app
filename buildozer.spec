[app]  
title = My Kivy App  
package.name = mykivyapp  
package.domain = org.test  
source.dir = .  
source.include_exts = py,png,jpg,kv,atlas  
version = 0.1  
requirements = python3,kivy==2.3.0  
orientation = portrait  
  
# አንድሮይድ ስሪቶች  
android.api = 33  
android.minapi = 21  
android.ndk = 25b  
android.archs = arm64-v8a,   
android.allow_backup = True  
  
# የጥንካሬ መመሪያዎች  
p4a.branch = master  
fullscreen = 0  
  
[buildozer]  
log_level = 2  
warn_on_root = 1
