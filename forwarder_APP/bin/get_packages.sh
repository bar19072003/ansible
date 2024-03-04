#!/bin/bash

# Monitor last 5 installed packages and versions

INSTALLED_PACKAGES=$(rpm -qa | tail -n5)
echo "installed_packages::$INSTALLED_PACKAGES"
