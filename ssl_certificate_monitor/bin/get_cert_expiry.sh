#!/bin/bash

# Monitor certificate expiration date

CERT_PATH="/etc/ssl/certs/ca-bundle.trust.crt"
EXPIRY_DATE=$(openssl x509 -noout -enddate -in $CERT_PATH | awk -F'=' '{print $2}')

echo "certificate_expiry_date::$EXPIRY_DATE"

# Monitor server version

SERVER_VERSION=$(lsb_release -a 2>/dev/null | grep "Release" | awk '{print $2}')
echo "server_version::$SERVER_VERSION"

# Monitor last 5 installed packages and versions

INSTALLED_PACKAGES=$(rpm -qa | tail -n5)
echo "installed_packages::$INSTALLED_PACKAGES"
