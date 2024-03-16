#!/usr/bin/env python3

# Monitor last 5 installed packages and versions

import subprocess

installed_packages = subprocess.check_output(["rpm", "-qa"]).decode("utf-8").splitlines()
print("The lsat 5 packages installed on the server are: ")
for p in installed_packages[-5:]:
    print(p)