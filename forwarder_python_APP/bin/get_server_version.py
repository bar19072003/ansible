#!/usr/bin/env python3

# Monitor server version

import subprocess

server_version_info = subprocess.check_output(["lsb_release", "-a"]).decode("utf-8").splitlines()
server_version = [line.split()[1] for line in server_version_info if "Release" in line][0]
print(f"The server version is : {server_version}")

