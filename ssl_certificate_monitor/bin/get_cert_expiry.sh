#!/bin/bash

CERT_PATH="/etc/ssl/certs/ca-bundle.trust.crt"
EXPIRY_DATE=$(openssl x509 -noout -enddate -in $CERT_PATH | awk -F'=' '{print $2}')

echo "certificate_expiry_date::$EXPIRY_DATE"

