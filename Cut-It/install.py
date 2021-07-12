"""
    Installs system-appropriate modules
"""

import pip

# Non platform specific modules
try:
    with open('requirements.txt', 'r') as f:
        general_modules = [(line.strip()).split() for line in f]

except Exception:
    general_modules = None

# Windows only modules
try:
    with open('windows.txt', 'r') as f:
        windows_modules = [(line.strip()).split() for line in f]

except Exception:
    windows_modules = None

# Linux only modules
try:
    with open('linux.txt', 'r') as f:
        linux_modules = [(line.strip()).split() for line in f]

except Exception:
    linux_modules = None

# MacOS only modules
try:
    with open('darwin.txt', 'r') as f:
        darwin_modules = [(line.strip()).split() for line in f]

except Exception:
    darwin_modules = None

# Installs every module in a supplied list of modules
def install(modules):
    [pip.main(['install', module]) for module in modules]

# Installs appropriate modules
if __name__ == '__main__':

    from sys import platform

    if general_modules:
        install(general_modules)

    if (platform == 'windows') and (windows_modules):
        install(windows_modules)

    elif (platform == 'linux') and (linux_modules):
        install(linux_modules)

    elif (platform == 'darwin') and (darwin_modules):
        install(darwin_modules)