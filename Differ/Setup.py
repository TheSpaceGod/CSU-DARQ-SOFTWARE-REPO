#!/usr/bin/python

try:
    import pip
    print("\nInstalling Differ dependencies.")
    pip.main(['install','bsdiff4'])
    print("Differ install done.\n")
except Exception:
    print("Differ setup failed. This setup requires 'python-pip'; if not installed, please install it.")
