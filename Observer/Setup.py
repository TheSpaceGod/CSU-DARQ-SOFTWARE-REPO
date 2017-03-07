#!/usr/bin/python

try:
    import pip
    print("\nInstalling Observer dependencies.")
    pip.main(['install','watchdog'])
    print("Observer install done.\n")
except Exception:
    print("Differ setup failed. This setup requires 'python-pip'; if not installed, please install it.")