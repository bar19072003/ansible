#!/usr/bin/env python3

# This script monitor certificate expiration date

import datetime
import subprocess

def get_cert_expiry(cert_path):
    try:
        cert_info = subprocess.check_output(["openssl", "x509", "-noout", "-enddate", "-in", cert_path]).decode("utf-8")
        expiry_date_str = cert_info.strip().split("=")[1]
        expiry_date = datetime.datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        return expiry_date
    except subprocess.CalledProcessError as e:
   /home/bar/ansible/forwarder_python_APP     print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

cert_path = "/etc/ssl/certs/ca-bundle.trust.crt"
expiry_date = get_cert_expiry(cert_path)
print(f"certificate_expiry_date::{expiry_date}")
