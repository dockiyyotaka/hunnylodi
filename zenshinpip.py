import os
import subprocess

modules = [
    "requests", "colorama", "rich", "cfonts"
]

for mod in modules:
    try:
        __import__(mod)
    except ImportError:
        print(f"Installing {mod}...")
        subprocess.run(["pip", "install", mod], check=True)

print("✅ All required modules are installed!")
